import psutil

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80


def collect_system_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return cpu, memory, disk


def display_metrics(cpu, memory, disk):
    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")


def check_thresholds(cpu, memory, disk):
    if cpu > CPU_THRESHOLD:
        print("High CPU Usage Alert")

    if memory > MEMORY_THRESHOLD:
        print("High Memory Usage Alert")

    if disk > DISK_THRESHOLD:
        print("High Disk Usage Alert")


def main():
    cpu, memory, disk = collect_system_metrics()
    display_metrics(cpu, memory, disk)
    check_thresholds(cpu, memory, disk)


if __name__ == "__main__":
    main()
