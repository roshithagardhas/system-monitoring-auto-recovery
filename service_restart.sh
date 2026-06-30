#!/bin/bash

# ==========================================
# System Monitoring & Auto-Recovery
# Service Recovery Script
# ==========================================

SERVICE="nginx"

check_service() {

    echo "========================================="
    echo "Service Status Check"
    echo "Time: $(date)"
    echo "========================================="

    if systemctl is-active --quiet "$SERVICE"
    then
        echo "[INFO] $SERVICE service is running."

    else
        echo "[WARNING] $SERVICE service is down."
        echo "[INFO] Attempting to restart..."

        sudo systemctl restart "$SERVICE"

        if systemctl is-active --quiet "$SERVICE"
        then
            echo "[SUCCESS] $SERVICE restarted successfully."
        else
            echo "[ERROR] Failed to restart $SERVICE."
        fi
    fi
}

main() {
    check_service
}

main
