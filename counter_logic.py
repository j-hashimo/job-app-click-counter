# Logic for handling counter operations

def increment_counter(current_value):
    """
    Increment the counter by 1.
    Args:
        current_value (int): The current counter value.
    Returns:
        int: Updated counter value.
    """
    return current_value + 1


def decrement_counter(current_value):
    """
    Decrement the counter by 1.
    Args:
        current_value (int): The current counter value.
    Returns:
        int: Updated counter value.
    """
    return current_value - 1


def reset_counter():
    """
    Reset the counter to 0.
    Returns:
        int: The reset counter value (0).
    """
    return 0
