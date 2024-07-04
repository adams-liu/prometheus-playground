# Dockerfile
FROM python:3.9-slim

# Install cron
RUN apt-get update && apt-get install -y cron && apt-get install -y procps

# Install Prometheus Client
RUN pip install prometheus_client

# Set up the application directory
WORKDIR /usr/src/app

# Copy the Python script and crontab file
COPY job_script.py .
COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab

# Apply the cron job
RUN crontab /etc/cron.d/crontab

# Ensure the cron service is started
CMD ["cron", "-f"]