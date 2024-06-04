### help(fun_name)

# ====== 1 - Count lines in a file that do not start with T ====== 

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
  

# ====== 2. Count the number of palindromic substrings in the given string ====== 

def count_palindromic_substrings(s):
    n = len(s)
    count = 0
    
    for i in range(n):
        # Odd length palindromes
        count += expand_around_center(s, i, i)
        # Even length palindromes
        count += expand_around_center(s, i, i + 1)
        
    return count

def expand_around_center(s, left, right):
    count = 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        count += 1
        left -= 1
        right += 1
    return count

print("==========\n\n")
string = "ababa"
result = count_palindromic_substrings(string)
print("Number of palindromic substrings:", result)
print("\n\n==========")


# ======  3. Find occurrence of "the" in a file ====== 

def count_occurrences_of_the(file_path):
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            words = line.lower().split()
            count += words.count("the")
    return count

file_path = 'example.txt'  # replace with your file path
result = count_occurrences_of_the(file_path)
print("Number of occurrences of 'the':", result)


# ====== 4. Find max length of common substring without repeating char ======

def length_of_longest_substring(s):
    char_map = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_map:
            left = max(left, char_map[s[right]] + 1)
        char_map[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length


def lowest_substring_without_repetition(s):
    char_set = set()
    left = 0
    min_length = float('inf')
    start_index = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        if right - left + 1 < min_length:
            min_length = right - left + 1
            start_index = left

    return s[start_index:start_index + min_length]


string = "abcabcbb"
print(f"String : {string}")
result = length_of_longest_substring(string)
print("Max length of substring without repeating characters:", result)
result = lowest_substring_without_repetition(string)
print("Lowest length substring without repeating characters:", result)


# ======= 5. Read a file and tokenize each line and store the lines in a tuple and print the tuple =======

def tokenize_file_lines(file_path):
    tokens = []
    with open(file_path, 'r') as file:
        for line in file:
            tokens.append(tuple(line.split()))
    return tuple(tokens)

file_path = 'example.txt'  
result = tokenize_file_lines(file_path)
print("Tokenized lines as tuples:", result)


# ======= 6. Print the valid parentheses with the value of n =======

def generate_parentheses(n):
    result = []
    generate_all_combinations(result, "", n, n)
    return result

def generate_all_combinations(result, current, open_remain, close_remain):
    if open_remain == 0 and close_remain == 0:
        result.append(current)
        return
    if open_remain > 0:
        generate_all_combinations(result, current + "(", open_remain - 1, close_remain)
    if close_remain > open_remain:
        generate_all_combinations(result, current + ")", open_remain, close_remain - 1)

# Example usage
n = 3
result = generate_parentheses(n)
print("Valid parentheses combinations for n =", n, ":", result)




# ===== 7. Read the content of a text file to generate tuples, then categorize these tuples into different lists based on their types: string, character, and integer ===== 

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


# ====== 8. count no of lines, words and char ======

def countLinesWordsChar(file_path,lines,words,chars):
    with open(file_path,mode='r') as file:
    # file = open(file_path,mode='r')
        for line in file:
            lines+=1
            list_of_words = line.strip().split() 
            words += len(list_of_words) 
            chars += len(line) 
            # print(f"split {list_of_words}")


    return lines, words, chars

print("==============\n")
file_path = "countLinesWordsChar.txt"
words = chars = lines = 0
lines, words, chars = countLinesWordsChar(file_path,lines,words,chars)
print(f"No of lines in the file : {lines}")
print(f"No of words in the file : {words}")
print(f"No of chars in the file : {chars}")

print("\n==============")
