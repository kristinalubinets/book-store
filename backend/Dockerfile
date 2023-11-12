# Use the official Python image from Docker Hub as the base image
FROM python:3.9

# Set environment variables for PostgreSQL connection
ENV POSTGRES_DB=mydatabase
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_HOST=db
ENV POSTGRES_PORT=5432

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt requirements.txt

# Install dependencies using pip
RUN pip install -r requirements.txt

# Copy the application code to the container
COPY ./app /app

# Expose the port your FastAPI application will run on (adjust as needed)
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]