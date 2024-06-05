# count no of lines, words and char
# count line starting with 'T'
# count no of times 'the' appeared in the file

# count no of lines, words and char
def countLinesWordsChar(file_path):
  file = open(file_path,mode='r')
  words = ch = lines = 0
  for line in file:
    lines+=1
    list_of_words = line.strip().split()
    words+=len(list_of_words)
    # ch +=len(line)
    for wordss in list_of_words:
      ch= ch+len(wordss)

  return lines,words,ch

# count line starting with 'T'
def countLinesStartsWithT(filepath):
  cnt = 0
  file = open(filepath,mode='r')
  for line in file: 
    # print("type of line: ",type(line))  # string
    # if not line.startswith('T'):
    if line[0] == 't' or line[0] =='T':
      cnt+=1

  return cnt

def countTheInFile(filepath):
  cnt = 0
  f = open(filepath,mode='r')
  for line in f:
    line = line.lower().strip()
    cnt+=line.count('the')

  return cnt

print("=============\n\n")
file_path = "End_term/endterm.txt"

words = ch = lines = 0
lines, words, ch = countLinesWordsChar(file_path)
print(f"No of lines in the file : {lines}")
print(f"No of words in the file : {words}")
print(f"No of chars in the file : {ch}")

cnt = countLinesStartsWithT(file_path)
print(f"\nNo of Lines starts with T: {cnt}")

# string = "py is the best"
# cnt = string.count('the')

cnt = countTheInFile(file_path)
print(f"\nNo of time 'the' appeared in the file: {cnt}")

print("\n\n=============")
