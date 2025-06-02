import os
from dotenv import load_dotenv
import chainlit as cl
from litellm import completion
import json

# Load the environment variables from the .env file
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

@cl.on_chat_start
async def start():
    """Set up the chat session when a user connects."""
    # Initialize an empty chat history in the session.
    cl.user_session.set("chat_history", [])

    await cl.Message(content="Welcome to the Anas Ahmed AI Assistant! How can I help you today?").send()

@cl.on_message
async def main(message: cl.Message):

    loader = cl.Message(content="Thinking...")
    await loader.send()

    history = cl.user_session.get("chat_history") or []
    history.append({"role": "user", "content": message.content})

    full_response = ""

    try:
        stream = completion(
            model="gemini/gemini-2.0-flash",
            api_key=gemini_api_key,
            messages=history,
            stream=True  
        )

        await loader.remove()
        msg = cl.Message(content="")
        await msg.send()
        for chunk in stream:
            token = chunk["choices"][0]["delta"].get("content") or ""
            full_response += token
            await msg.stream_token(token)
            print(token, end="", flush=True)  

        await msg.update()

        history.append({"role": "assistant", "content": full_response}) 
        cl.user_session.set("chat_history", history)

    except Exception as e:
        msg.content = f"Error: {str(e)}"
        await msg.update()
        print(f"Error: {str(e)}")


@cl.on_chat_end
async def on_chat_end():
    # Retrieve the full chat history at the end of the session
    history = cl.user_session.get("chat_history") or []
    # Save the chat history to a file (or persist it elsewhere)
    with open("chat_history.json", "w") as f:
        json.dump(history, f, indent=2)
    print("Chat history saved.")
