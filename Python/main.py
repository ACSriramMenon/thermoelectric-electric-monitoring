import matplotlib
matplotlib.use("TkAgg")

import tkinter as tk
import subprocess
import sys
import os
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

USE_FAKE = True
SERIAL_PORT = "COM5"
BAUD = 9600

if USE_FAKE:
    script_path = os.path.join(os.path.dirname(__file__), "temp_data.py")
    process = subprocess.Popen([sys.executable, script_path], stdout = subprocess.PIPE, text = True)

    def read_line():
        return process.stdout.readline().strip()
else:
    import serial
    ser = serial.Serial(SERIAL_PORT, BAUD)

    def read_line():
        return ser.readline().decode().strip()

root = tk.Tk()
root.title("TEG Smart Energy Monitor")
root.geometry("1000x600")
root.configure(bg = "#0f172a")

container = tk.Frame(root, bg = "#0f172a")
container.pack(fill = "both", expand = True, padx = 20, pady = 10)

main_area = tk.Frame(container, bg = "#0f172a")
main_area.pack(fill = "both", expand = True)

header_frame = tk.Label(main_area, bg = "#0f172a")
header_frame.pack(fill = "x", pady = (15, 10))

title = tk.Label(header_frame, text = "THERMOELECTRIC ENERGY MONITORING SYSTEM", font = ("Segoe UI", 22, "bold"), bg = "#0f172a", fg = "white")
title.pack(anchor="center")

subtitle = tk.Label(header_frame, text = "Real-Time Voltage Monitoring System using TEG", font = ("Segoe UI", 12), bg = "#0f172a", fg = "#9ca3af")
subtitle.pack(anchor="center", pady = (5, 0))

card_frame = tk.Frame(main_area, bg = "#0f172a")
card_frame.pack(fill = "x", padx = 25, pady = (10, 5))

def create_card(parent, text):
    frame = tk.Frame(parent, bg = "#1f2937", padx = 20, pady = 15)
    label = tk.Label(frame, text = text, font = ("Segoe UI", 10), bg = "#1f2937", fg = "#9ca3af")
    value = tk.Label(frame, text = "--", font = ("Segoe UI", 22, "bold"), bg = "#1f2937", fg = "#22d3ee")
    label.pack(anchor = "w")
    value.pack(anchor = "w")
    frame.pack(side = "left", padx = 12, pady = 5)
    return value

volt_value = create_card(card_frame, "Voltage (V)")
status_value = create_card(card_frame, "System Status")

graph_container = tk.Frame(main_area, bg = "#0f172a")
graph_container.pack(fill = "both", expand = True, padx = 25, pady = 15)

graph_frame = tk.Frame(graph_container, bg = "#1f2937", padx = 15, pady = 15)
graph_frame.pack(fill = "both", expand = True)

fig = Figure(figsize = (6, 3), dpi = 100)
ax = fig.add_subplot(111)

fig.patch.set_facecolor("#1f2937")
ax.set_facecolor("#1f2937")

canvas = FigureCanvasTkAgg(fig, master = graph_frame)
canvas.get_tk_widget().pack(fill = "both", expand = True)

plot_line, = ax.plot([], [], linewidth = 2)

x_data = []
y_data = []

def get_status(voltage):
    if voltage > 2:
        return "Good", "green"
    elif voltage > 1:
        return "Moderate", "yellow"
    else:
        return "Low", "red"

def parse(line):
    try:
        return float(line.split(':')[1])
    except:
        return None

def update():
    line = read_line()

    if line:
        v = parse(line)

        if v is not None:
            volt_value.config(text = f"{v:.2f}")

            status, color = get_status(v)
            status_value.config(text = status, fg = color)

            x_data.append(len(x_data))
            y_data.append(v)

            if len(x_data) > 50:
                x_data.pop(0)
                y_data.pop(0)

            plot_line.set_data(x_data, y_data)
            ax.relim()
            ax.autoscale_view()

            ax.set_title("Voltage Output", color = "white", fontsize = 12)
            ax.tick_params(colors = "white")

            for spine in ax.spines.values():
                spine.set_color("#374151")

            ax.grid(alpha = 0.2, linestyle = "--")

            canvas.draw()

    root.after(1500, update)

def on_closing():
    if USE_FAKE:
        try:
            process.terminate()
        except:
            pass
    root.destroy()

update()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()