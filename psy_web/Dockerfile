# ---------- assets builder (Node) ----------
FROM node:20-alpine AS assets-builder

WORKDIR /app/frontend

# Install frontend dependencies (will generate package-lock.json if missing)
COPY frontend/package.json ./
RUN npm install

# Ensure output directories exist (webpack/gulp write to ../static/...)
RUN mkdir -p /app/static/js /app/static/css

# Copy source code needed for asset build
COPY frontend/ ./

# Build JS and CSS assets
RUN npx webpack && npx gulp


# ---------- runtime (Python) ----------
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VIRTUALENVS_CREATE=false

# Set the working directory inside the container
WORKDIR /psy_web

# Install runtime system dependencies (pg_isready used in entrypoint)
RUN apt-get update && apt-get install -y \
    postgresql-client \
  && rm -rf /var/lib/apt/lists/*

# Install Python dependencies with better layer caching
COPY requirements.txt /psy_web/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . /psy_web

# Copy built assets from the Node builder
COPY --from=assets-builder /app/static /psy_web/static

# Set the Python path
ENV PYTHONPATH=/psy_web

# Ensure entrypoint is executable
RUN chmod +x /psy_web/entrypoint.sh

# Define the entrypoint for the container
ENTRYPOINT ["/psy_web/entrypoint.sh"]