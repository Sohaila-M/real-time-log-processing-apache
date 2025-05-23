#!/bin/bash

LOG_FILE="/home/bigdata/flume-logs/realtime/app.log"

generate_random_ip() {
    echo "$((RANDOM%255)).$((RANDOM%255)).$((RANDOM%255)).$((RANDOM%255))"
}


generate_log_line() {
    IP=$(generate_random_ip)
    TIMESTAMP=$(date "+[%d/%b/%Y:%H:%M:%S +0000]")
    REQUEST="GET / HTTP/1.1"
    STATUS_CODE=$(shuf -i 200-500 -n 1)
    SIZE=$(shuf -i 100-5000 -n 1)
    echo "$IP - - $TIMESTAMP \"$REQUEST\" $STATUS_CODE $SIZE"
}

while true; do
    generate_log_line >> "$LOG_FILE"
    sleep 2  
done
