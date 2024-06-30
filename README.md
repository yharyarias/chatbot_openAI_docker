# Chatbot using OpenAI API and Docker

This project demonstrates how to create a chatbot using the OpenAI API and Dockerize it for easy deployment.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [1. Create an OpenAI Account](#1-create-an-openai-account)
  - [2. Obtain API Key from OpenAI](#2-obtain-api-key-from-openai)
  - [3. Setting Up Your Project](#3-setting-up-your-project)
  - [4. Developing the Chatbot](#4-developing-the-chatbot)
  - [5. Configuring Environment Variables](#5-configuring-environment-variables)
  - [6. Creating the Docker Image](#6-creating-the-docker-image)
- [Testing and Troubleshooting](#testing-and-troubleshooting)
- [Additional Considerations](#additional-considerations)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This repository contains a Python-based chatbot powered by the OpenAI API. The chatbot interacts with users in natural language, providing responses based on AI-generated content. The project demonstrates how to Dockerize the chatbot application, enabling seamless deployment across different environments.

## Prerequisites

Before starting, ensure you have the following:

- An OpenAI account
- Python installed on your machine
- Docker Desktop installed (for Dockerizing the application)
- Visual Studio Code or any preferred code editor

## Setup Instructions

Follow these steps to set up and run the chatbot application:

### 1. Create an OpenAI Account

If you haven't already, sign up for an OpenAI account at [OpenAI](https://www.openai.com).

### 2. Obtain API Key from OpenAI

After creating your account:

- Log in to the OpenAI platform.
- Navigate to the API section.
- Generate an API key to authenticate API requests.

### 3. Setting Up Your Project

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/chatbot-openai-docker.git
   ```
2. Navigate into the project directory:
   
   ```bash
   cd chatbot-openai-docker
   ```
3. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

### 4. Developing the Chatbot

1. Install required Python dependencies:

  ```bash
  pip install -r requirements.txt
  ```
2. Develop the chatbot script (chatbot.py) using the OpenAI API. Example code snippets are provided in the repository.
   
### 5. Configuring Environment Variables

1. Create a `.env` file in the project root:

  ```bash
  touch .env
  ```

2. Add your OpenAI API key to the `.env` file:

  ```bash
  OPENAI_API_KEY=your_api_key_here
  ```
  Replace your_api_key_here with the API key obtained from OpenAI.
  
3. Use the dotenv package to load environment variables in your Python script securely.

### 6. Running the Docker Image

1. Ensure you have Docker Desktop installed and running on your machine.

2. Set your OpenAI API key in Dockerfile:

  ```bash
  # Set the environment variable for the OpenAI API key
  ENV OPENAI_API_KEY="your_api_key_here"
  ```
3. Build the Docker image using the `docker build -t chatbot-image .` command.
4. `Use docker run -it chatbot-imagen:latest` to start the container.
5. Test the chatbot functionality to ensure it interacts correctly with the OpenAI API.

## Testing and Troubleshooting
Continue with the testing and troubleshooting sections as previously outlined in the README.

## Additional Considerations
Continue with the additional considerations section as previously outlined in the README.

## Contributing
Continue with the contributing section as previously outlined in the README.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

   
