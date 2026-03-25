#!/usr/bin/env python3
import psutil
import platform
import socket
import subprocess
import time
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.live import Live

console = Console()
last_net_io = psutil.net_io_counters()

def get_gpu_model():
    try:
        cmd = "lspci | grep -E 'VGA|3D' | head -n 1"
        result = subprocess.check_output(cmd, shell=True).decode()
        return result.split(': ')[-1].strip()
    except:
        return "Unknown"

def get_cpu_temp():
    try:
        temps = psutil.sensors_temperatures()
        for name in ['coretemp', 'cpu_thermal', 'k10temp', 'acpitz']:
            if name in temps:
                return f"{temps[name][0].current}°C"
        return "N/A"
    except:
        return "N/A"

def get_net_speed():
    global last_net_io
    new_net_io = psutil.net_io_counters()
    download = (new_net_io.bytes_recv - last_net_io.bytes_recv) / 1024 / 1024
    upload = (new_net_io.bytes_sent - last_net_io.bytes_sent) / 1024 / 1024
    last_net_io = new_net_io
    return f"D: {download:.1f}MB/s | U: {upload:.1f}MB/s"

def create_table():
    cpu_overall = psutil.cpu_percent()
    cpu_cores = psutil.cpu_percent(percpu=True)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    table = Table(title=f"[bold cyan]System Dashboard[/bold cyan] | {datetime.now().strftime('%H:%M:%S')}", expand=True)
    
    table.add_column("Category", style="bold yellow")
    table.add_column("Details", style="white")
    table.add_column("Status", style="bold green", justify="right")

    table.add_row("OS/Kernel", f"{platform.system()} {platform.release()}", f"Temp: {get_cpu_temp()}")
    table.add_row("CPU Load", "Overall Usage", f"{cpu_overall}%")
    
    cores_data = " ".join([f"C{i}:{int(v)}%" for i, v in enumerate(cpu_cores)])
    table.add_row("Cores", cores_data, "")
    
    table.add_section()
    
    ram_bar = "█" * int(ram.percent / 10) + "░" * (10 - int(ram.percent / 10))
    table.add_row("Memory", f"{ram.used // 1024**2}MB / {ram.total // 1024**2}MB", f"{ram_bar} {ram.percent}%")
    
    disk_bar = "█" * int(disk.percent / 10) + "░" * (10 - int(disk.percent / 10))
    table.add_row("Disk (/)", f"{disk.free // 1024**3}GB Free", f"{disk_bar} {disk.percent}%")

    table.add_section()

    table.add_row("Network", get_net_speed(), f"IP: {socket.gethostbyname(socket.gethostname())}")
    table.add_row("GPU", get_gpu_model(), "[bold blue]Active[/bold blue]")
    
    return table

def main():
    with Live(create_table(), refresh_per_second=1, screen=True) as live:
        try:
            while True:
                time.sleep(1)
                live.update(create_table())
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    main()
