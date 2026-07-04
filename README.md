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
├── monitor.py           # Main application
├── monitoring.py        # System metrics collection
├── recovery.py          # Recovery workflow
├── config.py            # Configuration settings
├── service_restart.sh   # Linux recovery script
├── requirements.txt
├── README.md
├── logs/
│   └── monitor.log
└── .gitignore
```

## Features

- Real-time CPU monitoring
- Real-time Memory monitoring
- Real-time Disk monitoring
- Configurable threshold values
- Automatic logging using Python's `logging` module
- Threshold-based alert detection
- Automated recovery workflow
- Modular Python architecture
- Linux service recovery support
- Professional project structure

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

- Recovery script is currently a placeholder for Windows and is intended for Linux environments.
- Alerts are displayed in the terminal and log files only.
- Email or messaging notifications are not yet implemented.
- The project currently monitors a single system instance.
---

## Future Enhancements

- Email notifications
- Slack or Microsoft Teams integration
- Docker container support
- AWS EC2 deployment
- Prometheus metrics integration
- Grafana monitoring dashboard
- Multi-service monitoring
- Kubernetes health monitoring

---

## Learning Outcomes

Through this project, I gained practical experience in:

- Python-based system monitoring using the `psutil` library.
- Collecting and analyzing CPU, memory, and disk usage metrics.
- Building modular Python applications using multiple modules.
- Configuration management using a dedicated `config.py` file.
- Implementing structured logging with Python's `logging` module.
- Exception handling and application error management.
- Designing threshold-based alerting and automated recovery workflows.
- Linux service management and Bash scripting fundamentals.
- Organizing projects using professional software architecture principles.
- Version control using Git and GitHub with meaningful commits.
- Understanding basic DevOps and Site Reliability Engineering (SRE) concepts.
---

## License

This project is licensed under the MIT License.

---

## Author

**Gardhas Roshitha**

Aspiring System Development Engineer with interests in Linux, AWS, DevOps, Cloud Infrastructure, Automation, and System Reliability Engineering.

GitHub: https://github.com/roshithagardhas

---
