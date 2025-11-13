# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY pyproject.toml .

# Install any needed packages specified in requirements.txt
RUN  .

# Copy the rest of the application's code to the working directory
COPY . .

# Specify the command to run on container start
CMD ["python", "main.py"]