# Use the official base image of Python 3.11
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the source code and .env file to the container
COPY . .

# Install the necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable for the OpenAI API key
ENV OPENAI_API_KEY=""

# Command to execute the Python script
CMD ["python", "chatbot_docker.py"]
