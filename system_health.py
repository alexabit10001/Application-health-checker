import psutil
import time
from datetime import datetime

# Define thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

# Log file
LOG_FILE = "system_health.log"

def log_message(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")
    print(message)

def check_system_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent
    process_count = len(psutil.pids())

    log_message(f"CPU Usage: {cpu_usage}% | Memory Usage: {memory_usage}% | Disk Usage: {disk_usage}% | Processes: {process_count}")

    if cpu_usage > CPU_THRESHOLD:
        log_message(f"Alert: High CPU usage detected - ({cpu_usage}%)")

    if memory_usage > MEMORY_THRESHOLD:
        log_message(f"Alert: High Memory usage detected -({memory_usage}%)")

    if disk_usage > DISK_THRESHOLD:
        log_message(f"Alert : Low Disk Space -({disk_usage}%)")

if __name__ == "__main__":
    while True:
        check_system_health()
        time.sleep(10)  # check every 10 seconds



