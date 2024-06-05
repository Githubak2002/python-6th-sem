# # Count the number of palindromic substrings in the given string

def isPalindrom(str):
  start = 0
  end = len(str) - 1 
  while start < end:
    if str[start] != str[end]:
      return False
    end -= 1
    start += 1
  
  # print(str)
  return True

def countPalindroms(string):
  cnt = 0
  for x in range(len(string)):
    for y in range(x + 1, len(string) + 1):
      tmpString = string[x:y]
      if isPalindrom(tmpString):
        cnt += 1

  return cnt

print("=================\n")
str = "abba"
cnt = countPalindroms(str)

# # palin = isPalindrom(str)
# # print(f"String {str} is palindrom: {palin}")
# cnt = countPalindroms(str)

print(f"count: {cnt}")     

print("\n=================")