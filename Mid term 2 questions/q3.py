# 3. Find occurrence of "the" in a file

def count_occurrences_of_the(file_path):
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            # print(f"line - {line}")
            # line - hello pyhton
            words = line.lower().split()
            print(f"words - {words}")
            # words - ['hello', 'pyhton']
            count += words.count("the")
    return count

def countThis(file_path):
    cnt = 0
    with open(file_path,mode='r') as f:
        for line in f:
            words = line.lower().split()
            # print(words[0])
            if words[0] == 'hello':
                cnt+=1
    return cnt
            

print("===========\n\n")
file_path = 'example.txt' 
result = count_occurrences_of_the(file_path)
print("Number of occurrences of 'the':", result)

thisWord = countThis(file_path)
print("Number of occurrences of 'this':", thisWord)
print("\n\n===========")
