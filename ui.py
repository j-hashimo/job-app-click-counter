# Logic for creating the user interface
from tkinter import Tk, Label, Button
from counter_logic import increment_counter, decrement_counter, reset_counter
from file_handler import write_number_to_file

def create_ui(initial_counter_value):
    """
    Creates a simple UI for the counter application.
    Args:
        initial_counter_value (int): The initial counter value to display.
    """
    # Initialize the main application window
    root = Tk()
    root.title("Click Counter")

    # Counter state
    counter_value = {"value": initial_counter_value}

    # Update the counter display
    def update_display():
        counter_label.config(text=str(counter_value["value"]))

    # Increment button callback
    def increment_callback():
        counter_value["value"] = increment_counter(counter_value["value"])
        update_display()

    # Decrement button callback
    def decrement_callback():
        counter_value["value"] = decrement_counter(counter_value["value"])
        update_display()

    # Reset button callback
    def reset_callback():
        counter_value["value"] = reset_counter()
        update_display()

    # Save button callback
    def save_callback():
        write_number_to_file("counter.txt", counter_value["value"])

    # Create UI elements
    counter_label = Label(root, text=str(counter_value["value"]), font=("Helvetica", 24))
    counter_label.pack(pady=10)

    increment_button = Button(root, text="Increment", command=increment_callback)
    increment_button.pack(pady=5)

    decrement_button = Button(root, text="Decrement", command=decrement_callback)
    decrement_button.pack(pady=5)

    reset_button = Button(root, text="Reset", command=reset_callback)
    reset_button.pack(pady=5)

    save_button = Button(root, text="Save", command=save_callback)
    save_button.pack(pady=5)

    # Start the UI loop
    root.mainloop()
