# Use official Python image as base
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app
COPY . .

# Expose port (important for Render to detect)
EXPOSE 8000

# Run the app (for Flask)
# CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]

# OR Run the app (for FastAPI or Uvicorn-based apps)
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]
