# Use the official Python image as a base
FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY src/ ./

# Expose the port the app runs on
EXPOSE 8000

# Command to run the app with Gunicorn
# Run the application using Gunicorn with 4 worker processes (-w 4), 
# binding to all network interfaces on port 8000 (-b 0.0.0.0:8000), 
# and specifying the application entry point as "main:app".

# Production
# CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000", "main:app"]

# Development
# CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "--log-level", "debug", "main:app"]
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000", "--log-level", "debug", "main:app"]
