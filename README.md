<img width="1912" height="456" alt="image" src="https://github.com/user-attachments/assets/4ae60083-a9ae-4e7e-b2de-db29277419b6" />

# Terminal System Monitor

A terminal-based dashboard for real-time system resource monitoring. Built with Python, rich, and psutil. Optimized for Linux/Arch environments.

## Features
- CPU: Overall load, per-core usage, and temperature.
- Memory: Visual progress bar for RAM utilization.
- Storage: Free space monitoring for the root partition.
- Network: Real-time download and upload speeds in MB/s.
- GPU: Model detection via lspci.
- Interface: Interactive live-update screen similar to htop.

## Installation

### 1. Clone the repository
git clone (https://github.com/semenpro22gaempro-beep/system-monitor-linux.git)
cd your-repository

### 2. Install dependencies
pip install -r requirements.txt
# Note: On Arch Linux, use --break-system-packages if installing globally.

### 3. Install as a system command
To run the monitor using the "monitor" command from any directory:
pip install .

## Usage
Run the following command in your terminal:
monitor

Press Ctrl + C to exit.

## Requirements
- Python 3.7+
- psutil
- rich
- lm-sensors (required for CPU temperature readings)
