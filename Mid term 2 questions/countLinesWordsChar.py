#  count no of lines, words and char

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
