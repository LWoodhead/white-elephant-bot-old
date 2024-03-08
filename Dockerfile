# Python base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /discord_bot

#Upgrade pip 
RUN pip install --no-cache-dir --upgrade pip

ENV DISCORD_TOKEN=${DISCORD_TOKEN}

#Copy files into app directory
COPY discord_bot/classes discord_bot/main.py requirements.txt /discord_bot/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python", "main.py"]