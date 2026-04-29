# PROJECT OVERVIEW


# Thermoelectric Energy Monitoring System

This project implements a real-time monitoring system for electrical energy generated using a Thermoelectric Generator (TEG).
An Arduino is used to acquire voltage data, which is transmitted to a Python-based GUI for live visualization and analysis.

---

## Overview

The system converts heat energy into electrical energy using a TEG module.
The Arduino reads the generated voltage and sends it via serial communication to a Python application.
The Python interface processes this data and displays it in real time along with a graphical representation.

---

## Features

* Real-time voltage monitoring
* Live graphical visualization using Matplotlib
* Interactive GUI built with Tkinter
* Serial communication between Arduino and Python
* Simulation mode for testing without hardware

---

## Project Structure

```
Renewable_Energy/
├── python/
├── arduino/
├── docs/
└── README.md
```

---

## Hardware Components

* Arduino Uno
* Thermoelectric Generator (TEG) module
* Heat sinks (for maintaining temperature difference)
* Voltage sensor module
* Breadboard
* Jumper wires
* USB A–B cable

---

## Software Components

* Python 3
* Tkinter (GUI framework)
* Matplotlib (graph plotting)
* PySerial (serial communication)
* Arduino IDE

---

## How to Run

### 1. Upload Arduino Code

* Open `arduino/teg_monitor/teg_monitor.ino` in Arduino IDE
* Select the correct board and COM port
* Upload the code

---

### 2. Run Python Application

```
cd python
python main.py
```

---

## Configuration

Inside `main.py`:

* For simulation mode:

```
USE_FAKE = True
```

* For real hardware:

```
USE_FAKE = False
SERIAL_PORT = "COM3"
```

Ensure:

* Baud rate is set to 9600 in both Arduino and Python
* Arduino Serial Monitor is closed before running Python

---

## Output

* Displays real-time voltage readings
* Shows system status (Good / Moderate / Low)
* Plots voltage variation over time

---

## Documentation

Additional resources such as screenshots and circuit diagrams are available in the `Docs/` folder.

---

## Contribution

### Technical Development

* Designed and developed the Python GUI using Tkinter
* Implemented real-time data visualization using Matplotlib
* Established serial communication between Arduino and Python
* Structured and integrated the software components

### Team Contribution

This project was carried out as a group of 11 members, involving:

* Hardware setup and circuit assembly
* Data collection and testing
* Documentation and report preparation
* Presentation and demonstration

---

## Notes

The system focuses on voltage monitoring from the TEG module.
Temperature measurement was excluded due to sensor limitations during implementation.

---

## Future Scope

* Wireless data transmission (Bluetooth/Wi-Fi)
* Power output estimation and efficiency analysis
* Data logging and long-term monitoring
* Integration of advanced sensors

---

## Summary

This project demonstrates a complete pipeline from energy generation to real-time visualization:

Heat → Electrical Energy → Data Acquisition → Software Visualization
