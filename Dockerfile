# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt


RUN python manage.py migrate

# Make port 80 available to the world outside this container
EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]