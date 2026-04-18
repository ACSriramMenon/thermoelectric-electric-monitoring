import matplotlib
matplotlib.use("TkAgg")

import tkinter as tk
import subprocess
import sys
import os
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

USE_FAKE = True
SERIAL_PORT = "COM3"
BAUD = 9600

if USE_FAKE:
    script_path = os.path.join(os.path.dirname(__file__), "temp_data.py")
    process = subprocess.Popen([sys.executable, script_path], stdout=subprocess.PIPE, text=True)

    def read_line():
        return process.stdout.readline().strip()
else:
    import serial
    ser = serial.Serial(SERIAL_PORT, BAUD)

    def read_line():
        return ser.readline().decode().strip()

root = tk.Tk()
root.title("TEG Smart Energy Moniter")
root.geometry("1000x600")
root.configure(bg="#0f172a")

container = tk.Frame(root, bg="#0f172a")
container.pack(fill="both", expand=True, padx = 20, pady = 10)

main_area = tk.Frame(container, bg="#0f172a")
main_area.pack(fill="both", expand=True)

title = tk.Label(main_area, text = "TEG Energy Monitor", font = ("Segoe UI", 20, "bold"), bg = "#0f172a", fg = "white")
title.pack(anchor = "w", padx = 25, pady = (20, 10))

card_frame = tk.Frame(main_area, bg="#0f172a")
card_frame.pack(fill="x", padx=25, pady=10)

def create_card(parent, text):
    frame = tk.Frame(parent, bg="#1f2937", padx=20, pady=15)

    label = tk.Label(frame, text=text, font=("Segoe UI", 10), bg="#1f2937", fg="#9ca3af")
    value = tk.Label(frame, text="--", font=("Segoe UI", 22, "bold"), bg="#1f2937", fg="#22d3ee")

    label.pack(anchor="w")
    value.pack(anchor="w")

    frame.pack(side="left", padx=12, pady=5)
    return value

temp_value = create_card(card_frame, "Temperature (°C)")
volt_value = create_card(card_frame, "Voltage (V)")
status_value = create_card(card_frame, "System Status")

graph_container = tk.Frame(main_area, bg="#0f172a")
graph_container.pack(fill="both", expand=True, padx=25, pady=15)

graph_frame = tk.Frame(graph_container, bg="#1f2937", padx=15, pady=15)
graph_frame.pack(fill="both", expand=True)

fig = Figure(figsize=(6, 3), dpi=100)
ax = fig.add_subplot(111)

fig.patch.set_facecolor("#1f2937")
ax.set_facecolor("#1f2937")

canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.get_tk_widget().pack(fill="both", expand=True)

plot_line, = ax.plot([], [], linewidth=2)

x_data = []
y_data = []

def get_status(voltage):
    if voltage > 2:
        return "Good", "#22c55e"
    elif voltage > 1:
        return "Moderate", "#f59e0b"
    else:
        return "Low", "#ef4444"

def parse(line):
    try:
        temp, volt = line.split(',')
        t = float(temp.split(':')[1])
        v = float(volt.split(':')[1])
        return t, v
    except:
        return None, None

def update():
    line = read_line()

    if line:
        t, v = parse(line)

        if t is not None:
            temp_value.config(text=f"{t:.2f}")

        if v is not None:
            volt_value.config(text=f"{v:.2f}")

            status, color = get_status(v)
            status_value.config(text=status, fg=color)

            x_data.append(len(x_data))
            y_data.append(v)

            if len(x_data) > 50:
                x_data.pop(0)
                y_data.pop(0)

            plot_line.set_data(x_data, y_data)
            ax.relim()
            ax.autoscale_view()

            ax.set_title("Voltage Output", color="white", fontsize=12)
            ax.tick_params(colors="white")

            for spine in ax.spines.values():
                spine.set_color("#374151")

            ax.grid(alpha=0.2, linestyle="--")

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