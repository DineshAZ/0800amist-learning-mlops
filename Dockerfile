# Base Image for Building ML App
FROM python:3.9

# Working Directory
WORKDIR /mlapp

# Copy Requirements.txt, app.py, and data/rental_1000.csv
COPY . .  

# Libraries to install
RUN pip install --no-cache-dir -r requirements.txt

# Expose Port 5000
EXPOSE 5000

# Default Commands to run at start of Container
CMD ["python", "app.py"]

# Dockerfile was written by Siddarth
