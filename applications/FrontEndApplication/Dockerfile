# Use an official Python runtime as a parent image
FROM python:3.8-slim
# Expose port 4000 for the Flask app to run on
EXPOSE 4000
# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
# Define environment variable for Flask to run in production mode
ENV FLASK_ENV=production
# Run app.py when the container launches
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "4000"]

#docker build -t frontend-app
#docker run -p 4000:4000 frontend-app