# Import necessary modules
from counter_logic import increment_counter, decrement_counter, reset_counter
from file_handler import read_number_from_file, write_number_to_file
from ui import create_ui

# Entry point for the application
if __name__ == "__main__":
    # Load the counter value from the file if available, default to 0
    try:
        counter_value = read_number_from_file("counter.txt")
        if counter_value is None:
            counter_value = 0
    except Exception as e:
        print(f"Error loading counter from file: {e}")
        counter_value = 0

    # Create the UI and pass the counter value
    create_ui(counter_value)
