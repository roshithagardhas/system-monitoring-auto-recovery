
#!/bin/bash

set -u

SERVICE="nginx"

echo "========================================="
echo "Service Recovery Check"
echo "Time: $(date)"
echo "========================================="

if systemctl is-active --quiet "$SERVICE"; then
    echo "[INFO] $SERVICE is already running."
    exit 0
fi

echo "[WARNING] $SERVICE is down."
echo "[INFO] Attempting to restart $SERVICE..."

if ! systemctl restart "$SERVICE"; then
    echo "[ERROR] Restart command failed for $SERVICE."
    exit 1
fi

sleep 2

if systemctl is-active --quiet "$SERVICE"; then
    echo "[SUCCESS] $SERVICE restarted successfully."
    exit 0
else
    echo "[ERROR] $SERVICE is still inactive after restart."
    exit 1
fi
