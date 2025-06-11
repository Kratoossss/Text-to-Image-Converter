import os
import base64
import requests
import certifi
import streamlit as st
from llama_cpp import Llama

# Load the Llama language model once at the start (adjust the model path as needed)
llm = Llama(model_path="D:/ai-test/models/llama-2-7b.Q4_K_M.gguf")

def expand_prompt(prompt: str) -> str:
    """
    Expands a short prompt into a detailed, vivid description using the Llama language model.
    Args:
        prompt (str): The user's short prompt.
    Returns:
        str: The expanded, detailed prompt.
    """
    system_prompt = (
        "You are a creative assistant. Expand the following prompt into a vivid, detailed, artistic description for image generation.\n"
        "Prompt: "
    )
    full_prompt = system_prompt + prompt + "\nExpanded:"
    output = llm(full_prompt, max_tokens=128)
    return output["choices"][0]["text"].strip()

def generate_image(prompt: str) -> str:
    """
    Sends the expanded prompt to the Stability AI API to generate an image.
    Args:
        prompt (str): The expanded prompt for image generation.
    Returns:
        str: The file path to the saved generated image.
    Raises:
        ValueError: If the API key is missing or no image data is found in the response.
    """
    # Get the Stability API key from environment variables
    api_key = st.secrets["STABILITY_API_KEY"]
    if not api_key:
        raise ValueError("STABILITY_API_KEY is not set. Please set it in your environment.")

    # API endpoint and headers
    url = "https://api.stability.ai/v2beta/stable-image/generate/core"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json"
    }
    # Parameters for the image generation request
    files = {
        "model": (None, "stable-diffusion-v1-5"),
        "prompt": (None, prompt),
        "output_format": (None, "png"),
        "height": (None, "200"),
        "width": (None, "200"),
        "steps": (None, "30"),
        "samples": (None, "1"),
        "cfg_scale": (None, "7")
    }
    # Make the POST request to the API
    response = requests.post(url, headers=headers, files=files, verify=certifi.where())
    response.raise_for_status()
    data = response.json()

    image_base64 = None
    image_url = None

    # Parse the API response for image data
    if "image" in data:
        image_base64 = data["image"]
    elif "base64" in data:
        image_base64 = data["base64"]
    elif "url" in data:
        image_url = data["url"]
    elif "artifacts" in data:
        artifacts = data["artifacts"]
        if artifacts and isinstance(artifacts, list):
            artifact = artifacts[0]
            if "base64" in artifact:
                image_base64 = artifact["base64"]
            elif "url" in artifact:
                image_url = artifact["url"]

    # Save the image to a file
    output_image = os.path.join(os.path.dirname(__file__), "output.png")
    if image_base64:
        # If image is returned as base64, decode and save it
        with open(output_image, "wb") as f:
            f.write(base64.b64decode(image_base64))
        return output_image
    elif image_url:
        # If image is returned as a URL, download and save it
        img_response = requests.get(image_url)
        with open(output_image, "wb") as f:
            f.write(img_response.content)
        return output_image

    # If no image data found, raise an error
    raise ValueError("No image data found in API response")
