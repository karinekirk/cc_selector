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

