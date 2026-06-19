path = r"C:\Users\user\PycharmProjects\python-programs\.venv\Scripts\python.exe"



# Find the last '\' (before the file name)
last_slash = path.rfind("\\")

# Find the '\' before the last folder
previous_slash = path.rfind("\\", 0, last_slash)

# Extract the last folder name
folder = path[previous_slash + 1:last_slash]

print("Last Folder:", folder)

# ----------
path = r"C:\Users\user\PycharmProjects\python-programs\Classes\HemaSundar\Day03\extractWebsite.py"

parts = path.split("\\")

print("Last Folder:", parts[-2])