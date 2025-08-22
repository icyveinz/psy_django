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
    && npm install -g gulp-cli webpack webpack-cli

# Copy the project files into the container
COPY . /psy_web

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# RUN cd frontend && npm install

# Set the Python path
ENV PYTHONPATH=/psy_web

# Copy the entrypoint script and make it executable
COPY entrypoint.sh /psy_web/entrypoint.sh
RUN chmod +x /psy_web/entrypoint.sh

# Define the entrypoint for the container
ENTRYPOINT ["/psy_web/entrypoint.sh"]