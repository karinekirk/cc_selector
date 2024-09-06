import os
import json

def generate_sql_from_json(input_folder_path, output_sql_file, cross_ref_sql_file):
    # Get list of JSON files in the input folder
    json_files = [f for f in os.listdir(input_folder_path) if f.endswith('.json')]

    with open(output_sql_file, 'w') as sql_file, open(cross_ref_sql_file, 'w') as cross_ref_file:
        # Write the header for the SQL file (for the main Color_Curves table)
        sql_file.write("INSERT INTO Color_Curves (curve_id, curve_json)\nVALUES\n")

        # Write the header for the cross-reference file (for the Curve_File_Map table)
        cross_ref_file.write("INSERT INTO Curve_File_Map (curve_id, filename)\nVALUES\n")

        # Track if this is the first row for both tables
        first_row_main = True
        first_row_cross_ref = True

        # Loop through each JSON file and use an index as the curve_id
        for index, json_file in enumerate(json_files, start=1):  # 'start=1' to begin the index at 1
            curve_id = index  # Use the index as the curve_id
            json_path = os.path.join(input_folder_path, json_file)

            # Read and parse JSON data
            with open(json_path, 'r') as file:
                try:
                    curve_json = json.load(file)
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from file {json_file}")
                    continue

            # Convert Python object to a JSON string for SQL
            curve_json_str = json.dumps(curve_json).replace("'", "''")

            # Format the INSERT statement for the main table (Color_Curves)
            value_str_main = f"({curve_id}, '{curve_json_str}')"

            # Write the SQL INSERT command for the main table
            if first_row_main:
                sql_file.write(value_str_main)
                first_row_main = False
            else:
                sql_file.write(",\n" + value_str_main)

            # Format the INSERT statement for the cross-reference table (Curve_File_Map)
            value_str_cross_ref = f"({curve_id}, '{json_file}')"

            # Write the SQL INSERT command for the cross-reference table
            if first_row_cross_ref:
                cross_ref_file.write(value_str_cross_ref)
                first_row_cross_ref = False
            else:
                cross_ref_file.write(",\n" + value_str_cross_ref)

        # End both SQL statements
        sql_file.write(";\n")
        cross_ref_file.write(";\n")

if __name__ == "__main__":
    # Move up one folder and then into the Color_Curve_JSON folder
    input_folder_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Color_Curve_JSON')
    
    # Save the output files in the same directory as the script
    script_dir = os.path.dirname(__file__)
    output_sql_file = os.path.join(script_dir, 'init.colorcurves.sql')
    cross_ref_sql_file = os.path.join(script_dir, 'curve_file_map.sql')
    
    generate_sql_from_json(input_folder_path, output_sql_file, cross_ref_sql_file)
