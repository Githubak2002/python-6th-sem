# Count lines in a file that do not start with T

def count_lines_not_starting_with_T(file_path):
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            if not line.startswith('T'):
                count += 1
    return count


def count_lines_starting_with_T(file_path):
    cnt = 0
    with open(file_path,mode='r') as f:
        for line in f:
            words = line.split()
            print(words[0][0])
            # if not words[0][0] == 'T':
            if words[0][0] == 'T':
                cnt+=1
    return cnt

file_path = 'fileBasic.txt'  
result = count_lines_not_starting_with_T(file_path)
print("Number of lines not starting with 'T':", result)




    