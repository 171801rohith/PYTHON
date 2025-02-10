import requests
import json

# Replace with your actual Eden AI API key
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZGE0MjgxNzAtYzY3ZC00ZGEwLTllMzMtMmQ2NDhkZDU1NWVjIiwidHlwZSI6ImFwaV90b2tlbiJ9.leed4653GQvBNKksOU61o0gPQI8KQ-qiBaVyGWzidD8"

# Define the image generation parameters
payload = {
    "providers": ["stabilityai"],  # Specify the provider (e.g., stabilityai, deepai)
    "text": "A majestic dragon flying over a medieval castle",  # The prompt for image generation
    "width": 512,  # Desired width of the image
    "height": 512,  # Desired height of the image
    "steps": 50, # Number of diffusion steps (higher values = more detail, but longer generation time)
    "model_id": "stable-diffusion-xl-1024-v1-0", # Example Stable Diffusion model. Check Eden AI documentation for available models.
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Make the API request
try:
    response = requests.post("https://api.edenai.io/v2/image/generation", headers=headers, json=payload)
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

    result = response.json()

    # Extract the generated image URL
    image_url = result["generated_images"][0]["url"]  # Assuming you only generate one image

    # Download the image (optional)
    image_response = requests.get(image_url, stream=True)
    image_response.raise_for_status()

    with open("generated_image.jpg", "wb") as f:
        for chunk in image_response.iter_content(1024):
            f.write(chunk)

    print(f"Image saved to generated_image.jpg")
    print(f"Image URL: {image_url}")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    if response.status_code != 200:
        print(f"Response content: {response.text}") # Print error from API if available
except (KeyError, IndexError) as e:
    print(f"Error parsing JSON response: {e}")
    print(f"Response content: {response.text}")  # Print the full response for debugging