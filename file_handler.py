# Logic for handling file operations

def read_number_from_file(filename):
    """
    Reads an integer from a file.
    Args:
        filename (str): Path to the file.
    Returns:
        int or None: The integer value read from the file, or None if invalid.
    """
    try:
        with open(filename, 'r') as file:
            data = file.read().strip()
            # Ensure the content is an integer
            if data.isdigit() or (data.startswith('-') and data[1:].isdigit()):
                return int(data)
            else:
                print(f"Invalid data in file: {data}")
                return None
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None
    except Exception as e:
        print(f"Error reading file {filename}: {e}")
        return None


def write_number_to_file(filename, number):
    """
    Writes an integer to a file.
    Args:
        filename (str): Path to the file.
        number (int): The integer to write to the file.
    """
    try:
        with open(filename, 'w') as file:
            file.write(str(number))
    except Exception as e:
        print(f"Error writing to file {filename}: {e}")
