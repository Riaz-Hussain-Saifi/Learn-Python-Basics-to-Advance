# main.py: Main script that imports and uses functions from app.py and utils.py
# Demonstrates importing modules, using aliases, and the __name__ guard

# Import specific function from app.py
from app import greet

# Import with alias for convenience
import utils as ut

def main():
    """Main function to demonstrate module imports and usage."""
    # Use function from app.py
    user_name = "Bob"
    print(greet(user_name))
    
    # Use function from utils.py
    print(f"Sum of 3 and 4: {ut.add_numbers(3, 4)}")
    
    # Use another function from utils.py
    print(f"Is 10 even? {ut.is_even(10)}")

# Ensure main() only runs when main.py is executed directly
if __name__ == "__main__":
    print("Starting the main program")
    main()