# program to read and write a file
import os
def read_file(file_path):
    """Read the contents of a file and return as a list of lines."""
    if not os.path.exists(file_path):
        print(f"⚠️ File not found: {file_path}")
        return []

    with open(file_path, 'r') as file:
        return file.readlines()

def write_file(file_path, lines):
    """Write a list of lines to a file."""
    with open(file_path, 'w') as file:
        file.writelines(lines)
    print(f"✅ Successfully written to {file_path}")

def append_to_file(file_path, lines):
    """Append a list of lines to a file."""
    with open(file_path, 'a') as file:
        file.writelines(lines)
    print(f"✅ Successfully appended to {file_path}")

def file_exists(file_path):
    """Check if a file exists."""
    return os.path.exists(file_path)

def delete_file(file_path):
    """Delete a file if it exists."""
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"✅ Successfully deleted {file_path}")
    else:
        print(f"⚠️ File not found: {file_path}")

def get_file_size(file_path):
    """Get the size of a file in bytes."""
    if os.path.exists(file_path):
        return os.path.getsize(file_path)
    else:
        print(f"⚠️ File not found: {file_path}")
        return 0