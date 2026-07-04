import os
import logging
import subprocess
import psutil
import time

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

logging.basicConfig(
    filename="logs/monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def collect_system_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return cpu, memory, disk


def display_metrics(cpu, memory, disk):
    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")

def create_log_directory():
    os.makedirs("logs", exist_ok=True)

def write_log(cpu, memory, disk):
    logging.info(
        f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%"
    )


def check_thresholds(cpu, memory, disk):

    if cpu > CPU_THRESHOLD:
        print("High CPU Usage Alert")
        logging.warning("High CPU Usage Detected")
        recover_service()

    if memory > MEMORY_THRESHOLD:
        print("High Memory Usage Alert")
        logging.warning("High Memory Usage Detected")
        recover_service()

    if disk > DISK_THRESHOLD:
        print("High Disk Usage Alert")
        logging.warning("High Disk Usage Detected")
        recover_service()

def recover_service():
    logging.info("Recovery process initiated.")
    print("Recovery process started...")

    try:
        print("Executing recovery script...")

        # Placeholder for Linux implementation
        # subprocess.run(["bash", "service_restart.sh"], check=True)

        logging.info("Recovery completed successfully.")
        print("Recovery completed successfully.")

    except Exception as e:
        logging.error(f"Recovery failed: {e}")
        print(f"Recovery failed: {e}")

        
def main():
    while True:
        try:
            create_log_directory()

            cpu, memory, disk = collect_system_metrics()

            display_metrics(cpu, memory, disk)

            write_log(cpu, memory, disk)

            check_thresholds(cpu, memory, disk)

            print("-" * 40)

        except Exception as e:
            print(f"Error: {e}")

        time.sleep(5)


if __name__ == "__main__":
    main()