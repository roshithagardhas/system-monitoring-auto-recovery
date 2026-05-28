#!/bin/bash

SERVICE="nginx"

if ! systemctl is-active --quiet $SERVICE
then
    echo "$SERVICE is down. Restarting..."
    sudo systemctl restart $SERVICE
    echo "$SERVICE restarted successfully."
else
    echo "$SERVICE is running."
fi
