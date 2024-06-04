# 2. Count the number of palindromic substrings in the given string

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

