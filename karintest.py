import random
import json
from PIL import Image, ImageDraw

# Define the color schemes table with actual colors
color_schemes_table = {
    'Mono': ['Base Color'],
    'Ana': ['Base Color', 'Analogous Color'],
    'Comp': ['Base Color', 'Complementary Color'],
    'Sp': ['Base Color', 'Split-Complementary Color'],
    'Tri': ['Base Color', 'Triadic Color'],
    'Sq': ['Base Color', 'Square Color'],
    'Rect': ['Base Color', 'Rectangular Color']
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

# Function to generate a random color curve
def generate_random_curve(color_schemes_table):
    # Placeholder for code to generate a random color curve
    random_color_curve = {
        'ColorScheme': random.choice(list(color_schemes_table.keys())),
        'Complexity': random.randint(1, 5),
        'CurveData': {
            'floatCurves': [
                {
                    'keys': [{'time': random.uniform(0, 1), 'value': random.uniform(0, 1)} for _ in range(10)]
                }
            ]
        }
    }
    return random_color_curve

# Generate a random color curve
random_color_curve = generate_random_curve(color_schemes_table)
color_scheme = random_color_curve['ColorScheme']
complexity = random_color_curve['Complexity']

# Create a PNG file to visualize the color curve using Pillow
width, height = 800, 600
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)
points = [(int(key['time'] * width), int(key['value'] * height)) for key in random_color_curve['CurveData']['floatCurves'][0]['keys']]

# Ensure the color scheme has the required number of color elements
color_data = color_schemes_table.get(color_scheme)

if color_data and len(color_data) > 1:
    rgb_color_data = color_data[1][:3]  # Take only the first 3 elements for RGB

    try:
        # Convert the color data to integers for visualization
        visualization_color = tuple(int(255 * channel) for channel in rgb_color_data)

    except (ValueError, TypeError):
        # Fallback color in case of invalid RGB data
        visualization_color = (255, 0, 0)  # Red color as fallback

    # Visualize the color curve using the converted color
    draw.line(points, fill=visualization_color, width=2)

    # Save the image to a file with the corrected naming convention
    image_filename = f"CC_karin_{color_scheme}.png"
    image.save(image_filename)

    print(f"Created color curve visualization and saved as '{image_filename}'.")
else:
    print(f"Error: Color data not available for the selected color scheme '{color_scheme}'. Please check the color schemes table.")
    