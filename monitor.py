
import os
import logging
import time
import subprocess

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

SERVICE = "nginx"

os.makedirs(LOG_DIRECTORY, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def write_log(cpu, memory, disk):
    logging.info(
        f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%"
    )


def check_thresholds(cpu, memory, disk):
    if cpu > CPU_THRESHOLD:
        print("High CPU Usage Alert")
        logging.warning("High CPU Usage Detected")

    if memory > MEMORY_THRESHOLD:
        print("High Memory Usage Alert")
        logging.warning("High Memory Usage Detected")

    if disk > DISK_THRESHOLD:
        print("High Disk Usage Alert")
        logging.warning("High Disk Usage Detected")


def check_service_health():
    result = subprocess.run(
        ["systemctl", "is-active", "--quiet", SERVICE],
        check=False,
        timeout=10,
    )

    if result.returncode == 0:
        print(f"Service Health: {SERVICE} is active.")
        logging.info("%s service is active.", SERVICE)
        return

    print(f"Service Alert: {SERVICE} is not active.")
    logging.warning("%s service is not active. Starting recovery.", SERVICE)

    recovered = recover_service()

    if recovered:
        logging.info("%s recovery completed successfully.", SERVICE)
        print(f"Recovery verified for {SERVICE}.")
    else:
        logging.error("%s recovery failed.", SERVICE)
        print(f"Recovery failed for {SERVICE}. Check the logs.")


def main():
    print("System Monitoring & Auto-Recovery started.")
    logging.info("Monitoring started.")

    while True:
        try:
            cpu, memory, disk = collect_system_metrics()

            display_metrics(cpu, memory, disk)
            write_log(cpu, memory, disk)
            check_thresholds(cpu, memory, disk)
            check_service_health()

            print("-" * 40)

        except KeyboardInterrupt:
            print("\nMonitoring stopped by user.")
            logging.info("Monitoring stopped by user.")
            break

        except Exception:
            logging.exception("Unexpected monitoring error.")
            print("Monitoring error. Check the log for details.")

        time.sleep(MONITOR_INTERVAL)


if __name__ == "__main__":
    main()
