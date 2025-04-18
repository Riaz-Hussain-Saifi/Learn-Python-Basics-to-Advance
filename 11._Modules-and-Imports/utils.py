# utils.py: Additional utility module with simple helper functions
# Demonstrates creating another reusable module

def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

def is_even(num):
    """Return True if the number is even, False otherwise."""
    return num % 2 == 0

# Optional: Code to test utils.py when run directly
if __name__ == "__main__":
    print("Testing utils.py")
    print(f"2 + 3 = {add_numbers(2, 3)}")
    print(f"Is 4 even? {is_even(4)}")