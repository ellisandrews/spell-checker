# Set base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /spell-checker

# Copy the code to the working directory
COPY . .

# Install the dependencies
RUN pip install -r requirements.txt

# Expose the port where the app runs in the container
EXPOSE 5000
