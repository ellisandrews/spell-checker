# Set base image (host OS)
FROM python:3.8

# Set the working directory in the container
WORKDIR /spell-checker

# Copy the code to the working directory
COPY . .

# Install the dependencies
RUN pip install -r requirements.txt

# Set flask specific environment variables
ENV FLASK_APP spell_checker
ENV FLASK_RUN_HOST 0.0.0.0

# Expose the port where the app runs
EXPOSE 5000
