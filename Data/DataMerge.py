#Merge chat
def process_dialogues(file_path):
    """
    Processes dialogues from a text file to create input-output pairs.
    Consecutive lines from the same speaker are merged together.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    dialogue_pairs = []
    current_input = []
    current_output = []
    
    for line in lines:
        line = line.strip()
        if line.startswith("user:"):
            if current_output:  # If there was an ongoing output, save the dialogue pair
                dialogue_pairs.append(("\t".join([" ".join(current_input), " ".join(current_output)])))
                current_input = []  # Reset for the next dialogue pair
                current_output = []
            current_input.append(line[5:].strip())  # Add to current input
        elif line.startswith("me:") and (current_input or current_output):
            current_output.append(line[3:].strip())  # Add to current output

    # Don't forget the last pair, if any
    if current_input and current_output:
        dialogue_pairs.append(("\t".join([" ".join(current_input), " ".join(current_output)])))

    return dialogue_pairs

def save_dialogues(dialogue_pairs, output_file_path):
    """
    Saves the processed dialogue pairs to a file.
    """
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for pair in dialogue_pairs:
            file.write(pair + "\n")

# Replace these paths with your actual file paths
input_file_path = 'reverted_data.txt'
output_file_path = 'merged_file.txt'

# Process the dialogues and save them to a new file
dialogue_pairs = process_dialogues(input_file_path)
save_dialogues(dialogue_pairs, output_file_path)

print(f"Processed dialogue pairs have been saved to: {output_file_path}")

