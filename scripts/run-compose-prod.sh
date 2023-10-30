#!/bin/bash

# Navigate to the directory where docker-compose.yml is located
cd $(dirname "$0")/..

# # Load environment variables from .env.prod
# export $(grep -v '^#' ./.env.prod | xargs)

# Load only http_proxy and https_proxy variables from .env.prod
export http_proxy=$(grep -E '^http_proxy=' ./.env.prod | cut -d '=' -f 2-)
export https_proxy=$(grep -E '^https_proxy=' ./.env.prod | cut -d '=' -f 2-)

# Run Docker Compose
docker compose -f docker-compose.prod.yml up -d --build
