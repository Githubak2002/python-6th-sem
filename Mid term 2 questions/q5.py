# 6. Read a file and tokenize each line and store the lines in a tuple and print the tuple

def tokenize_file_lines(file_path):
    tokens = []
    with open(file_path, 'r') as file:
        for line in file:
            tokens.append(tuple(line.split()))
    return tuple(tokens)

# Example usage
file_path = 'example.txt'  # replace with your file path
result = tokenize_file_lines(file_path)
print("Tokenized lines as tuples:", result)
