# Use a specific Python base image for stability
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 5000

# Command to run the API
CMD ["python", "api.py"]

