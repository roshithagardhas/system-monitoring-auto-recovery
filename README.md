# System Monitoring & Auto-Recovery Tool

A Linux system monitoring and automated service recovery tool built with Python, Bash, and `psutil`. The project demonstrates practical DevOps and Site Reliability Engineering (SRE) concepts, including system resource monitoring, service health checks, automated remediation, and logging.

## Project Overview

The application continuously monitors CPU, memory, and disk utilization. It checks the health of the Nginx service and automatically invokes a Bash recovery script if the service becomes inactive.

The recovery script attempts to restart Nginx and verifies whether the service becomes active. Monitoring and recovery events are recorded in a log file for troubleshooting and operational visibility.

## Technologies Used

- **Language:** Python 3
- **Scripting:** Bash
- **Operating System:** Linux (Ubuntu)
- **Metrics Collection:** `psutil`
- **Service Management:** `systemctl`
- **Example Service:** Nginx
- **Logging:** Python `logging` module
- **Version Control:** Git and GitHub

## Features

- Continuous CPU, memory, and disk utilization monitoring
- Configurable resource thresholds
- Threshold-based terminal alerts
- Nginx service health monitoring
- Python-triggered automated service recovery
- Bash-based service restart and post-restart verification
- Structured application logging
- Exception handling and recovery timeout handling
- Modular Python architecture
- Graceful shutdown using Ctrl+C

## Project Structure

```text
system-monitoring-auto-recovery/
├── monitor.py           # Main monitoring loop and service health checks
├── monitoring.py        # System metrics collection and display
├── recovery.py          # Executes and handles the recovery workflow
├── config.py            # Thresholds, interval, and log configuration
├── service_restart.sh   # Bash-based Nginx recovery and verification
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── logs/
│   └── monitor.log      # Runtime monitoring and recovery logs
└── .gitignore
```

## Architecture

```text
System Resources
       |
       v
CPU / Memory / Disk Metrics
       |
       v
Python Monitoring Loop
       |
       +----------------------+
       |                      |
       v                      v
Threshold Checks        Nginx Health Check
                              |
                    +---------+---------+
                    |                   |
                    v                   v
                  Active             Inactive
                    |                   |
                    v                   v
              Continue Loop       recovery.py
                                        |
                                        v
                                service_restart.sh
                                        |
                                        v
                                 Restart Nginx
                                        |
                                        v
                              Verify Service Status
                                        |
                                        v
                                 Log the Outcome
```

## Prerequisites

- Linux system with systemd (Ubuntu recommended)
- Python 3
- pip
- Bash
- Git
- Nginx
- Sufficient permissions to check and restart the Nginx service

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/roshithagardhas/system-monitoring-auto-recovery.git
cd system-monitoring-auto-recovery
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Install Nginx if it is not already installed

On Ubuntu:

```bash
sudo apt update
sudo apt install nginx
```

Confirm the service is available:

```bash
systemctl is-active nginx
```

The monitoring script needs appropriate system permissions to check and restart the service.

## Configuration

Update `config.py` to adjust the monitoring behavior.

Default settings:

- CPU threshold: 80%
- Memory threshold: 80%
- Disk threshold: 80%
- Monitoring interval: 5 seconds

The application writes monitoring and recovery events to `logs/monitor.log`.

## Usage

### Run the monitoring application

From the project directory, with the virtual environment activated:

```bash
python monitor.py
```

The application continuously collects system metrics and checks Nginx health. Press `Ctrl+C` to stop monitoring gracefully.

### Run the recovery script independently

```bash
bash service_restart.sh
```

This script checks Nginx status, attempts a restart if the service is inactive, and verifies the resulting service state.

### View recent logs

```bash
tail -n 80 logs/monitor.log
```

## Validation and Testing

The following end-to-end test was performed on a Linux environment:

1. Confirmed that Nginx was active.
2. Stopped Nginx to simulate a service failure.
3. Started the Python monitoring application.
4. Confirmed that Python detected the inactive service.
5. Confirmed that Python invoked the recovery workflow.
6. Verified that the Bash script restarted Nginx successfully.
7. Observed subsequent monitoring cycles reporting that Nginx was active.
8. Checked the log file for detection, recovery, and service health events.

### Evidence from the test

```text
Service Alert: nginx is not active.
Recovery process started...
[WARNING] nginx is down.
[INFO] Attempting to restart nginx...
[SUCCESS] nginx restarted successfully.
Recovery script completed successfully.
Recovery verified for nginx.
Service Health: nginx is active.
```

The log file recorded the recovery event and subsequent successful health checks. The final `systemctl is-active nginx` check returned `active`.

## Current Limitations

- The application currently monitors a single configured service: Nginx.
- Resource alerts are reported in the terminal and log file.
- External notification integrations are not implemented.
- The application is intended for Linux systems using systemd.
- Threshold alerts currently report high resource utilization; they do not automatically remediate CPU, memory, or disk pressure.

## Future Enhancements

- Email, Slack, or Microsoft Teams notifications
- Monitoring multiple services
- AWS EC2 deployment and operational automation
- Prometheus metrics integration
- Grafana monitoring dashboards
- Docker container health monitoring
- Kubernetes health checks
- Improved alerting, reporting, and recovery metrics

## Learning Outcomes

This project provided practical experience with:

- Collecting system metrics using Python and `psutil`
- Configurable threshold-based monitoring
- Linux service management using `systemctl`
- Bash scripting and automated service recovery
- Integrating Python monitoring with shell scripts
- Structured logging and exception handling
- Validating recovery outcomes
- Modular application design
- Git-based version control
- DevOps and SRE principles such as service health checks, remediation, and availability

## License

This project is licensed under the MIT License.

## Author

**Gardhas Roshitha**

Aspiring System Development Engineer interested in Linux, AWS, DevOps, cloud infrastructure, automation, and Site Reliability Engineering.

GitHub: https://github.com/roshithagardhas
