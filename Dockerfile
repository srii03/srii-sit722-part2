# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable for the database URL
ENV DATABASE_URL=postgresql://lib_postgres_db_user:vABkDXl758bv3Gz6LaQeSPc8WWpwCosA@dpg-crtog2u8ii6s73agc630-a.oregon-postgres.render.com/lib_postgres_db?sslmode=require

# Run app.py when the container launches
CMD ["uvicorn", "book_catalog.main:app", "--host", "0.0.0.0", "--port", "8000"]

