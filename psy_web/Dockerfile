# Use the official Python 3.11 slim image as the base
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VIRTUALENVS_CREATE=false

# Set the working directory inside the container
WORKDIR /psy_web

# Install system dependencies and Node.js
RUN apt-get update && apt-get install -y \
    postgresql-client \
    curl \
    build-essential \
    && curl -fsSL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g gulp-cli webpack webpack-cli \
    && rm -rf /var/lib/apt/lists/*

# Copy package files first for better Docker layer caching
COPY frontend/package.json frontend/package-lock.json /psy_web/frontend/

# Install Node.js dependencies
RUN cd /psy_web/frontend && npm ci

# Copy the rest of the application
COPY . /psy_web

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create static directory structure for frontend build output
RUN mkdir -p /psy_web/static/css /psy_web/static/js

# Build frontend assets (this will create the static files)
RUN cd /psy_web/frontend && \
    npx webpack --mode=production && \
    npx gulp

# Set the Python path
ENV PYTHONPATH=/psy_web

# Copy the entrypoint script and make it executable
COPY entrypoint.sh /psy_web/entrypoint.sh
RUN chmod +x /psy_web/entrypoint.sh

# Define the entrypoint for the container
ENTRYPOINT ["/psy_web/entrypoint.sh"]