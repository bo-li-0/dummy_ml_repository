# Use an official Python runtime as a parent image
FROM python:3.8-slim

# set the working dir in the container
WORKDIR /app

# copy the current directory contents into the container at /app
COPY . /app

# install any needed packages specified in requirements.txt
RUN pip install --nocache-dir -r requirements.txt

# make port 80 available to the world outside this container
EXPOSE 80

# Run run.py when the container launches
CMD ["python", "run.py"]