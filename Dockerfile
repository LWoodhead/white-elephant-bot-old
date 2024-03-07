# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /discord_bot

# Copy the current directory contents into the container at /app
RUN pip install --no-cache-dir --upgrade pip

COPY discord_bot/classes /discord_bot
COPY discord_bot/main.py /discord_bot
COPY requirements.txt /discord_bot

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python", "main.py"]