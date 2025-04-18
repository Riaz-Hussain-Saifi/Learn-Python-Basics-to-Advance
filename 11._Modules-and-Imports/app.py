# app.py: Utility module containing reusable functions
# This module demonstrates how to create functions that can be imported elsewhere

def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}! Welcome to the app."

def calculate_square(num):
    """Return the square of a given number."""
    return num * num

# Example of code that should only run when app.py is executed directly
if __name__ == "__main__":
    print("Running app.py directly")
    print(greet("Alice"))
    print(f"Square of 5: {calculate_square(5)}")