import json

def load_config(config_path="config.json"):
    """
    Loads the configuration file from the specified path.

    Uses File I/O to open the file and the json module
    to parse its contents into a Python dictionary.

    Args:
        config_path (str): The path to the config.json file.

    Returns:
        dict: The configuration data.
    """
    try:
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
            return config
    except FileNotFoundError:
        print(f"Error: File not found at: '{config_path}'")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode json at '{config_path}'")
        
if __name__ == "__main__":
    config = load_config()
    if config:
        print("Config loaded successfully:")    
        print(f"Base URL: {config.get('base_url')}")
        print(f"Browser: {config.get('browser')}")