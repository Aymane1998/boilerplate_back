#!/bin/bash

# Navigate to the base directory
cd $(dirname "$0")/..

# load environment variables from .env.local
set -a; source .env.local; set +a;

# Run Docker Compose
python manage.py runserver