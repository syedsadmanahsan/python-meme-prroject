import os
import random
from PIL import Image, ImageDraw, ImageFont

class MemeGenerator:
    def __init__(self, font_path, font_size=40):
        self.font_path = font_path
        self.font_size = font_size
        self.font = ImageFont.truetype(font_path, font_size)

    def generate_meme(self, image_path, top_text, bottom_text, output_path):
        try:
            # Open the image file
            img = Image.open(image_path)

            # Convert the image to RGB mode
            img = img.convert("RGB")

            # Initialize drawing context
            draw = ImageDraw.Draw(img)

            # Calculate text sizes
            top_text_width, top_text_height = draw.textbbox((0, 0), top_text, font=self.font)[2:]
            bottom_text_width, bottom_text_height = draw.textbbox((0, 0), bottom_text, font=self.font)[2:]

            # Calculate text positions
            width, height = img.size
            top_x = (width - top_text_width) / 2
            bottom_x = (width - bottom_text_width) / 2

            # Optionally vary vertical positions randomly for fun
            top_y = 10
            bottom_y = height - bottom_text_height - 10

            # Add text to image with shadow effect
            shadow_offset = 2
            shadow_color = "black"
            draw.text((top_x - shadow_offset, top_y - shadow_offset), top_text, font=self.font, fill=shadow_color)
            draw.text((bottom_x - shadow_offset, bottom_y - shadow_offset), bottom_text, font=self.font, fill=shadow_color)
            
            # Generate random text color (bright colors)
            text_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            draw.text((top_x, top_y), top_text, font=self.font, fill=text_color)
            draw.text((bottom_x, bottom_y), bottom_text, font=self.font, fill=text_color)

            # Save the meme
            img.save(output_path)

            print(f"Meme generated successfully! Saved to {output_path}")

        except FileNotFoundError:
            print(f"Error: Image file '{image_path}' not found.")

        except Exception as e:
            print(f"Error: An unexpected error occurred - {e}")

if __name__ == "__main__":
    # Set font path and size
    font_path = os.path.join(os.path.dirname(__file__), "arial.ttf")
    font_size = 40

    # Create a MemeGenerator instance
    meme_generator = MemeGenerator(font_path, font_size)

    # Generate a meme
    image_path = os.path.join(os.path.dirname(__file__), "my_image.jpg")
    top_text = "When you finally understand NumPy"
    bottom_text = "But then you realize you still don't understand NumPy"
    output_path = os.path.join(os.path.dirname(__file__), "meme.jpg")
    meme_generator.generate_meme(image_path, top_text, bottom_text, output_path)