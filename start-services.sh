#!/bin/bash
# Start Client Portal Gateway and API service

# Start Client Portal Gateway with default config
bash bin/run.sh root/conf.yaml &

# Wait for gateway to start
sleep 10

# Start the API gateway
python3 main.py