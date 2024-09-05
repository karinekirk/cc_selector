import requests
import numpy as np
from PIL import Image

# Threshold for treating very small values as zero
EPSILON = 1e-6

def fetch_and_process_color_curve(source=None, is_api=True):
    """
    Fetch color curve data from API or use provided data, then process it.
    
    Parameters:
    - source (str): URL of the API (if is_api=True).
    - is_api (bool): If True, fetch data from API. If False, process provided data.
    """

    # Fetch data from API if source is an API URL
    if is_api:
        if source is None:
            raise ValueError("API URL must be provided when is_api is True.")
        response = requests.get(source)
        curve_data = response.json()  # Assume this is a list of curve data
    else:
        if source is None:
            raise ValueError("Sample data must be provided when is_api is False.")
        curve_data = source

    texture_width, texture_height = 256, 256

    # Initialize arrays for Red, Green, Blue, and Alpha
    red_normalized = np.zeros(texture_width)
    green_normalized = np.zeros(texture_width)
    blue_normalized = np.zeros(texture_width)
    alpha_normalized = np.ones(texture_width)  # Default alpha to fully opaque

    # Helper function to extract times and values, with fallback defaults
    def extract_curve_data(curve):
        if len(curve) == 1:
            # If there's only one key, treat it as a constant value
            constant_value = curve[0]['value']
            if abs(constant_value) < EPSILON:
                constant_value = 0
            return [0, 1], [constant_value, constant_value]  # Use constant across the entire range
        else:
            # Multiple keys; use times and values for interpolation
            times = [key['time'] for key in curve]
            values = [key['value'] for key in curve]
            # Treat values close to zero as zero
            values = [0 if abs(v) < EPSILON else v for v in values]
            return times, values

    for curve in curve_data:
        curve_id = curve['curve_id']
        float_curves = curve['curve_json']['floatCurves']

        if len(float_curves) != 4:
            print(f"Error: Curve ID {curve_id} does not have 4 float curves (red, green, blue, alpha).")
            continue

        try:
            # Process Red channel
            red_times, red_values = extract_curve_data(float_curves[0]['keys'])
            red_normalized = np.interp(np.linspace(0, 1, texture_width), red_times, red_values)

            # Process Green channel
            green_times, green_values = extract_curve_data(float_curves[1]['keys'])
            green_normalized = np.interp(np.linspace(0, 1, texture_width), green_times, green_values)

            # Process Blue channel
            blue_times, blue_values = extract_curve_data(float_curves[2]['keys'])
            blue_normalized = np.interp(np.linspace(0, 1, texture_width), blue_times, blue_values)

            # Process Alpha channel
            alpha_times, alpha_values = extract_curve_data(float_curves[3]['keys'])
            alpha_normalized = np.interp(np.linspace(0, 1, texture_width), alpha_times, alpha_values)

        except IndexError as e:
            print(f"Error processing Curve ID {curve_id}: {str(e)}")
            continue

        # Create an empty image for RGBA
        combined_image = np.zeros((texture_height, texture_width, 4), dtype=np.uint8)

        # Fill the image based on the RGBA curves
        for x in range(texture_width):
            combined_image[:, x, 0] = int(red_normalized[x] * 255)    # Red channel
            combined_image[:, x, 1] = int(green_normalized[x] * 255)  # Green channel
            combined_image[:, x, 2] = int(blue_normalized[x] * 255)   # Blue channel
            combined_image[:, x, 3] = int(alpha_normalized[x] * 255)  # Alpha channel

        # Convert numpy array to image
        combined_img = Image.fromarray(combined_image, 'RGBA')

        # Use the curve_id as part of the filename
        filename = f'color_curve_{curve_id}.png'
        combined_img.save(filename)

        print(f"Combined image saved as {filename}")

# Example usage with API
api_url = "http://localhost:8000/color-curves"  # Replace with actual API URL
fetch_and_process_color_curve(api_url, is_api=True)
