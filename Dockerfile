# Use a newer stable Python version (3.12) as the parent image
FROM python:3.12-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies needed for building packages
# This layer will be cached and only run when this command changes
RUN apt-get update && apt-get install -y build-essential libpq-dev \
    # Change #3: Clean up apt cache to reduce image size
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy only the requirements file first
COPY requirements.txt .

# Install Python dependencies. This layer will only be rebuilt
# if the requirements.txt file changes.
RUN pip install --no-cache-dir psycopg2-binary && \
    pip install --no-cache-dir -r requirements.txt

# Now, copy the rest of the application code. This is the part
# that will change most often.
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
