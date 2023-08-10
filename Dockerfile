# Use the official Python image as the base image
FROM python:3.8

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Set up a working directory
WORKDIR /Users/lokesh/Downloads/2022/web2/corider_assignment

# Copy requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port that the application runs on
EXPOSE 5000

# Run the application
CMD ["flask", "run"]
