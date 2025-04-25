# Use official lightweight Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app code
COPY . .

# Expose the port (Render needs this)
EXPOSE 10000

# Set environment variable for Flask
ENV FLASK_APP=app.py

# Run the app using gunicorn for production (optional but recommended)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:10000", "app:app"]
