FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install build essentials (kept minimal); useful for some wheels
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Keep the DB files or instance folder outside image layers if needed
VOLUME ["/app/instance"]

EXPOSE 5000

# Use gunicorn for production-like serving; App:app references the app object in App.py
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "App:app"]
