#First step, revert all file to single file
import os

# Specify the directory containing your files
directory_path = '../chat'

# Specify the path for the new merged file
merged_file_path = 'reverted_data.txt'

# List all files in the directory
file_names = sorted(os.listdir(directory_path))

# Open the merged file in write mode
with open(merged_file_path, 'w', encoding='utf-8') as merged_file:
    # Iterate over each file name
    for file_name in file_names:
        # Construct the full file path
        file_path = os.path.join(directory_path, file_name)
        
        # Ensure the path is indeed a file and not a directory/subdirectory
        if os.path.isfile(file_path):
            # Open and read the current file
            with open(file_path, 'r', encoding='utf-8') as file:
                # Read the content of the file
                content = file.read()
                
                # Write the content to the merged file, followed by two newlines
                merged_file.write(content + "\n\n")

print(f'All files have been merged into: {merged_file_path}')
