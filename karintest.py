import numpy as np
from PIL import Image
import random

# Define the color schemes table with actual colors
color_schemes_table = {
    'Mono': ['Base Color'],
    'Ana': ['Base Color', 'Analogous Color'],
    'Comp': ['Base Color', 'Complementary Color'],
    'Sp': ['Base Color', 'Split-Complementary Color'],
    'Tri': ['Base Color', 'Triadic Color'],
    'Sq': ['Base Color', 'Square Color'],
    'Rect': ['Base Color', 'Rectangular Color'],
    'Non': ['Base Color']  # Non-standard color scheme
}

# Populate the color schemes table with actual colors
base_color = (0.2, 0.4, 0.6)  # Base color in RGB
analogous_color = (0.2, 0.5, 0.6)  # Analogous color
complementary_color = (0.8, 0.6, 0.4)  # Complementary color
split_complementary_color = (0.2, 0.6, 0.7)  # Split-Complementary color
triadic_color = (0.3, 0.4, 0.6)  # Triadic color
square_color = (0.2, 0.5, 0.7)  # Square color
rectangular_color = (0.3, 0.5, 0.6)  # Rectangular color

color_schemes_table['Mono'].append(base_color)
color_schemes_table['Ana'].extend([base_color, analogous_color])
color_schemes_table['Comp'].extend([base_color, complementary_color])
color_schemes_table['Sp'].extend([base_color, split_complementary_color])
color_schemes_table['Tri'].extend([base_color, triadic_color])
color_schemes_table['Sq'].extend([base_color, square_color])
color_schemes_table['Rect'].extend([base_color, rectangular_color])

def create_color_channel_images(color_schemes_table):
    # Image dimensions
    texture_width, texture_height = 256, 256

    # Initialize an empty dictionary to store the images
    color_images = {}

    for color_scheme, colors in color_schemes_table.items():
        # Create an empty image for the color scheme
        color_image = np.zeros((texture_height, texture_width, 4), dtype=np.uint8)

        # Generate colors based on the color scheme data
        for x in range(texture_width):
            base_color = colors[1]  # Base color at index 1
            color_value = int((x / texture_width) * 255)
            color_image[:, x] = [int(channel * 255) if index < 3 else 255 for index, channel in enumerate(base_color)]

        # Convert the numpy array to an image
        color_img = Image.fromarray(color_image, 'RGBA')
        color_images[color_scheme] = color_img

        # Save the image with the color scheme name
        color_img.save(f'color_curve_texture_{color_scheme.lower()}_channel.png')

    print("Color channel images for the specified color schemes have been created and saved.")

# Call the function to create and save the images based on the color schemes table
create_color_channel_images(color_schemes_table)