import glob

# Use glob to find all files matching the pattern, and sort them alphabetically
filepaths = sorted(glob.glob('text_files/*.txt'))

# Iterate through each sorted file path
merged_content = []
for file_path in filepaths:
    # Open and read the file's content
    with open(file_path, 'r') as file:
        content = file.read()
        # Add the content to the list
        merged_content.append(content)

# Open the new file in write mode
with open('text_files/merged_file.txt', 'w') as merged_file:
    # Write each file's content into the merged file
    for content in merged_content:
        merged_file.write(content + "\n")  # Adding a newline for separation





