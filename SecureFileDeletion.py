import os
import random

def secure_delete_file():
    # Prompt the user for the file path
    file_path = input("Enter the file path: ")

    # Check if the file exists
    if not os.path.isfile(file_path):
        print("File not found.")
        return

    file_size = os.stat(file_path).st_size

    # Overwrite the file contents multiple times
    with open(file_path, "rb+") as file:
        passes = 3  # Number of passes
        for _ in range(passes):
            file.seek(0)
            random_data = bytearray(os.urandom(file_size))
            file.write(random_data)

    # Delete the file
    os.remove(file_path)
    print("Secure deletion completed.")

# Example usage
secure_delete_file()
