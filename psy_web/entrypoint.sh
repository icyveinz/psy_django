#!/bin/sh
set -e

# Wait for PostgreSQL
until pg_isready -h db -p 5432 -U user -d applications_db; do
  echo "Waiting for PostgreSQL..."
  sleep 2
done

echo "PostgreSQL is ready."

# Build frontend assets
echo "Building frontend assets..."
cd /psy_web/frontend
npm run build
cd /psy_web

# Run Django migrations
echo "Running Django migrations..."
python manage.py makemigrations wagtail_landing
python manage.py makemigrations a_blog
python manage.py makemigrations my_docs
python manage.py makemigrations users
python manage.py makemigrations core
python manage.py migrate

# Create superuser if it doesn't exist
echo "Creating superuser if not exists..."
python manage.py shell << EOF
from django.contrib.auth import get_user_model
import os

User = get_user_model()
username = os.getenv('DJANGO_SUPERUSER_USERNAME')
email = os.getenv('DJANGO_SUPERUSER_EMAIL')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

if username and email and password and not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"✅ Superuser '\${username}' created.")
else:
    print(f"ℹ️ Superuser '\${username}' already exists or environment variables not set.")
EOF

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Verify static files
echo "Checking static files..."
ls -la /psy_web/static/css/ || echo "CSS directory not found"
ls -la /psy_web/static/js/ || echo "JS directory not found"

# Start the app
echo "Starting Django..."
exec gunicorn psy_web.wsgi:application \
    --bind 0.0.0.0:8001 \
    --workers 1 \
    --threads 2 \
    --timeout 120 \
    --graceful-timeout 30 \
    --log-level info \
    --access-logfile - \
    --error-logfile -

# exec gunicorn --bind 0.0.0.0:8001 psy_web.wsgi:application для дева

# !!!!!!!!! Когда буду делать деплой на сервере с такой конфигурацией: 2 x 3.3 ГГц, 2гб РАМ
# gunicorn --bind 0.0.0.0:8001 -w 2 --threads 3 psy_web.wsgi:application