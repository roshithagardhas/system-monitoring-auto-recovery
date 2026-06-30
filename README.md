# System Monitoring & Auto-Recovery Tool

## Project Overview

The project demonstrates practical Linux administration, Python automation, Bash scripting, and basic DevOps and Site Reliability Engineering (SRE) concepts. It is designed to showcase how monitoring and automated recovery can improve system availability and reduce manual operational effort.# System Monitoring & Auto-Recovery Tool

## Technologies Used

- **Programming Language:** Python
- **Scripting:** Bash
- **Operating System:** Linux
- **Python Library:** psutil
- **Service Management:** systemctl
- **Example Service:** Nginx
- **Version Control:** Git & GitHub

## Project Structure

```text
system-monitoring-auto-recovery/
│
├── README.md             # Project documentation
├── monitor.py            # Monitors CPU, memory, and disk usage
├── service_restart.sh    # Automatically restarts the Nginx service
└── requirements.txt      # Python dependencies
```

## Features

- Monitors CPU utilization in real time.
- Monitors memory utilization.
- Monitors disk usage.
- Detects resource utilization beyond configured thresholds.
- Displays alerts when thresholds are exceeded.
- Checks the status of the Nginx service.
- Automatically restarts the service if it is not running.
- Designed for Linux system administration and automation tasks.

## Monitoring Architecture

```text
            Linux Server
                  │
      ┌───────────┼───────────┐
      ▼           ▼           ▼
    CPU       Memory       Disk
 Monitoring  Monitoring  Monitoring
      │           │           │
      └───────────┼───────────┘
                  ▼
          Python Monitoring
                Script
                  │
                  ▼
           Threshold Check
                  │
          ┌───────┴───────┐
          ▼               ▼
      Normal         Alert Triggered
                           │
                           ▼
                    Service Recovery
                    Restart Workflow
```


## Operational Capabilities

- CPU utilization monitoring
- Memory usage monitoring
- Disk utilization monitoring
- Threshold-based alerting
- Automated service recovery
- Linux operational troubleshooting
- System health visibility

  ## Prerequisites

Before running this project, ensure you have the following installed:

- Linux operating system (Ubuntu recommended)
- Python 3.x
- pip (Python package manager)
- Git
- Nginx
- Bash shell

  ## Installation

1. Clone the repository:

```bash
git clone https://github.com/roshithagardhas/system-monitoring-auto-recovery.git
```

2. Navigate to the project directory:

```bash
cd system-monitoring-auto-recovery
```

3. Install the required Python package:

```bash
pip install -r requirements.txt
```

## Usage

### Run the monitoring script

```bash
python monitor.py
```

### Run the service recovery script

```bash
bash service_restart.sh
```

## Sample Output

### Normal System

```text
CPU Usage: 35%
Memory Usage: 42%
Disk Usage: 58%

System resources are operating within normal limits.
```

### High Resource Utilization

```text
CPU Usage: 92%
High CPU Usage Alert

Checking Nginx service...
Nginx is down.
Restarting service...
Nginx restarted successfully.
```

---

## Current Limitations

- Threshold values are currently hardcoded in the Python script.
- The recovery script is configured to restart only the Nginx service.
- Monitoring is executed manually when the script is run.
- Alerts are displayed only in the terminal.
- Monitoring data is not stored in log files or a database.

---

## Future Enhancements

- Store threshold values in a configuration file.
- Implement continuous monitoring.
- Generate monitoring logs automatically.
- Monitor and recover multiple Linux services.
- Send alerts via Email or Slack.
- Build a web dashboard for monitoring system health.
- Containerize the application using Docker.
- Deploy the project on AWS EC2.

---

## Learning Outcomes

Through this project, I gained practical experience in:

- Python-based system monitoring using the `psutil` library.
- Bash scripting for Linux automation.
- Linux service management with `systemctl`.
- CPU, memory, and disk resource monitoring.
- Basic DevOps automation workflows.
- Linux troubleshooting and operational best practices.

---

## License

This project is licensed under the MIT License.

---

## Author

**Gardhas Roshitha**

Aspiring System Development Engineer with interests in Linux, AWS, DevOps, Cloud Infrastructure, Automation, and System Reliability Engineering.

GitHub: https://github.com/roshithagardhas

---
