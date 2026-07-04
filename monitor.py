import os
import logging
import time

from config import (
    CPU_THRESHOLD,
    MEMORY_THRESHOLD,
    DISK_THRESHOLD,
    MONITOR_INTERVAL,
    LOG_DIRECTORY,
    LOG_FILE,
)

from monitoring import collect_system_metrics, display_metrics
from recovery import recover_service

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def create_log_directory():
    os.makedirs(LOG_DIRECTORY, exist_ok=True)

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

        time.sleep(MONITOR_INTERVAL)


if __name__ == "__main__":
    main()