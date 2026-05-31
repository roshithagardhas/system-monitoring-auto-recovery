# System Monitoring & Auto-Recovery Tool

Linux monitoring and auto-recovery automation project built using Python and Bash scripting.

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
