# ===== 8. Read the content of a text file to generate tuples, then categorize these tuples into different lists based on their types: string, character, and integer ===== 

def categorize_tuples(file_path):
    string_list = []
    char_list = []
    int_list = []

    with open(file_path, 'r') as file:
        for line in file:
            tokens = line.split()
            for token in tokens:
                if token.isdigit():
                    int_list.append(int(token))
                elif len(token) == 1:
                    char_list.append(token)
                else:
                    string_list.append(token)
    
    return string_list, char_list, int_list

file_path = 'stringCharInt.txt'  # replace with your file path
strings, chars, ints = categorize_tuples(file_path)
print("Strings:", strings)
print("Characters:", chars)
print("Integers:", ints)
