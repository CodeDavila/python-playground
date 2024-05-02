import os

# Define file paths
path_letter = "Input/Letters/starting_letter.txt"
path_names = "Input/Names/invited_names.txt"
path_final_letter = "Output/ReadyToSend/"

# Read the example letter.
with open(path_letter, mode="r") as file:
    letter = file.readlines()

# Read the names.
with open(path_names, mode="r") as file:
    names = file.readlines()

# Prepare lines for each name
name_line = letter[0]
name_lines = []
for name in names:
    plain_name = name.replace("\n", "")
    new_name_line = name_line.replace("[name]", plain_name)
    name_lines.append(new_name_line)

# Remove name line from letter
letter = letter[1:len(letter)]

# Write personalized letters for each name
index = 0
for name in names:
    plain_name = name.replace("\n", "")
    new_path = path_final_letter + plain_name
    # Ensure directory exists or create it if not
    os.makedirs(os.path.dirname(new_path), exist_ok=True)
    with open(new_path, "w") as file:
        file.write(name_lines[index])
        for line in letter:
            file.write(line)
    index += 1
