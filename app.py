from openai import OpenAI
import requests
from PIL import Image
from io import BytesIO

# Set your OpenAI API key
openai = OpenAI(
    api_key='your-api-key',
)

def generate_image(prompt):
    response = openai.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    return image_url

def generate_variations(file_name):
    response = openai.images.create_variation(
        model="dall-e-2",
        image=open(file_name, "rb"),
        n=1,
        size="512x512"
    )
    image_url = response.data[0].url
    return image_url

def edit_image(prompt, image_path, mask_path):
    response = openai.images.edit(
        model="dall-e-2",
        image=open(image_path, "rb"),
        mask=open(mask_path, "rb"),
        prompt=prompt,
        n=1,
        size="512x512"
    )
    image_url = response.data[0].url
    return image_url

def display_image(image_url):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img.show()

if __name__ == "__main__":
    # Define your prompt for image generation
    prompt = "A futuristic cityscape with flying cars and neon lights"
    # Generate image
    image_url = generate_image(prompt)
    # Display the image
    display_image(image_url)

    # Generate variation
    image_url = generate_variations("cute_dog.png")
    # Display the image
    display_image(image_url)

    # Define your prompt for image editing
    prompt = "A swimming pool with toy duck floating"
    # Generate edited image
    image_url = edit_image(prompt, "swimming_pool.png", "swimming_pool_mask.png")
    # Display the image
    display_image(image_url)
