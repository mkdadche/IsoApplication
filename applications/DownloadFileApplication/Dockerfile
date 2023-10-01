# Use an official Python runtime as a parent image
FROM python:3.8-slim
# Expose port 4000 for the Flask app to run on
EXPOSE 4002
# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
# Define environment variable for Flask to run in production mode
ENV FLASK_ENV=production
# Run app.py when the container launches
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "4002"]

#docker build -t downloadfile-app .
#docker run -p 4002:4002 downloadfile-app