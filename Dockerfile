# Base image
FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run web server
CMD ["python", "webserver.py"]
