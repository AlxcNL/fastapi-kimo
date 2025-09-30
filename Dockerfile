# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Copy the current directory contents into the container at /code
COPY api /app

# Set the working directory to /app
WORKDIR /app

ADD requirements.txt .


# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]