from openai import OpenAI
import requests
from PIL import Image
from io import BytesIO

# Set your OpenAI API key
openai = OpenAI(
    api_key='sk-proj-BSBP9qsy2X5oAJI8jyF4T3BlbkFJpxYl353xSaDFNmGD08B6',
)

def generate_image(prompt):
    response = openai.images.generate(
        prompt=prompt,
        n=1,
        size="1024x1024"
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