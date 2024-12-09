import json

def synthesize_data(data, output_file="output.json"):
    """
    Save extracted data to a structured JSON file.
    Args:
        data (dict): Extracted data to be structured.
        output_file (str): Name of the output JSON file.
    """
    try:
        with open(output_file, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Data successfully saved to {output_file}")
    except Exception as e:
        print(f"Error saving data: {e}")

