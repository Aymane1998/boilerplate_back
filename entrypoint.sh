#!/bin/sh

# Run the migrations
# python manage.py makemigrations authentication
# python manage.py makemigrations api
python manage.py migrate

# # Wait for the migrations to finish
while python manage.py showmigrations | grep "\[ \]"; do
  echo "Waiting for migrations to finish..."
  sleep 2
done

echo 'Collecting static files...'
python manage.py collectstatic --no-input

# Execute the provided command
exec "$@"
