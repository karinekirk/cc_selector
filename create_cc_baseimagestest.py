import numpy as np
from PIL import Image

def create_color_channel_images():
    # Image dimensions
    texture_width, texture_height = 256, 256

    # Create empty images for red, green, and blue channels (RGBA)
    red_image = np.zeros((texture_height, texture_width, 4), dtype=np.uint8)
    green_image = np.zeros((texture_height, texture_width, 4), dtype=np.uint8)
    blue_image = np.zeros((texture_height, texture_width, 4), dtype=np.uint8)

    # Generate a simple gradient for demonstration
    for x in range(texture_width):
        # Create a gradient value from 0 to 255
        color_value = int((x / texture_width) * 255)

        # Fill the images with the color values
        red_image[:, x] = [color_value, 0, 0, 255]  # Red channel
        green_image[:, x] = [0, color_value, 0, 255]  # Green channel
        blue_image[:, x] = [0, 0, color_value, 255]  # Blue channel

    # Convert numpy arrays to images
    red_img = Image.fromarray(red_image, 'RGBA')
    green_img = Image.fromarray(green_image, 'RGBA')
    blue_img = Image.fromarray(blue_image, 'RGBA')

    # Save the imagescolor_curve_texture_2
    red_img.save('color_curve_texture_red_channel.png')
    green_img.save('color_curve_texture_green_channel.png')
    blue_img.save('color_curve_texture_blue_channel.png')

    print("Red, green, and blue channel images have been created and saved.")

# Call the function to create and save the images
create_color_channel_images()
