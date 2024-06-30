import os
from typing import List, Dict, Any
from openai import OpenAI, APIError
from dotenv import load_dotenv


def load_api_key() -> str:
    """
    Load the OpenAI API key from the environment variables.

    Returns:
        str: The OpenAI API key.

    Raises:
        ValueError: If the API key is not found in the environment variables.
    """
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        raise ValueError("OpenAI API key is not set. Make sure the .env file contains OPENAI_API_KEY.")
    
    return api_key


def create_openai_client(api_key: str) -> OpenAI:
    """
    Create an OpenAI client using the provided API key.

    Args:
        api_key (str): The OpenAI API key.

    Returns:
        OpenAI: The OpenAI client.
    """
    return OpenAI(api_key=api_key)


def get_assistant_response(client: OpenAI, messages: List[Dict[str, str]]) -> str:
    """
    Generate a response from the assistant based on the provided messages.

    Args:
        client (OpenAI): The OpenAI client.
        messages (List[Dict[str, str]]): The conversation history.

    Returns:
        str: The assistant's response.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.6,
            max_tokens=100
        )
        return response.choices[0].message.content
    
    except APIError as e:
        print(f"OpenAI API Error: {e}")
        return "I'm sorry, but I encountered an error while processing your request."


def main() -> None:
    """
    Main function to run the chat with the OpenAI assistant.
    """
    try:
        api_key = load_api_key()
        client = create_openai_client(api_key)
        
        messages = [
            {"role": "system", "content": "Absolutely, let's dive into Docker! Docker is a powerful tool used for containerization, allowing you to package your applications and all their dependencies into a standardized unit for software development."},
            {"role": "user", "content": "I'm a software engineer and I need to learn about Docker. Act as a Docker expert and teach me Docker from scratch, including exercises and evaluations."}
        ]
    
        while True:
            # Generate a response from the assistant
            assistant_response = get_assistant_response(client, messages)
            print("Assistant:", assistant_response)
            
            # Request new input from the user
            user_input = input("You: ")
            
            # Add the user's input to the conversation history
            messages.append({"role": "user", "content": user_input})
            
            # Add the assistant's response to the conversation history
            messages.append({"role": "assistant", "content": assistant_response})
    
    except ValueError as ve:
        print(f"ValueError: {ve}")
    
    except Exception as ex:
        print(f"Unexpected Error: {ex}")


if __name__ == "__main__":
    main()
