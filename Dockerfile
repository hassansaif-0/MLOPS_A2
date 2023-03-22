# Use an official Python runtime as a parent image
FROM python:3.10
# make a new directory webapp
RUN mkdir webapp
RUN mkdir -p /webapp

# Set the working directory in the container
WORKDIR /webapp

#copy everything 
COPY . .

RUN make install
RUN make format
RUN make lint

# Expose port 5000 for the Flask app to run on
EXPOSE 5000

# Define the command to run when the container starts
CMD ["python", "app.py"]
