#!/bin/bash

# Navigate to the directory where docker-compose.yml is located
cd $(dirname "$0")/..

# Run Docker Compose
docker compose -f docker-compose.prod.yml up -d --build
