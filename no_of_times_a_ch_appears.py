
# quest - 6.a.  count the numbers of characters in the string and store them in a dictionary data structure. 
def char_frequency(str1): 
  dict = {} 
  for n in str1: 
    keys = dict.keys() 
    if n in keys: 
      dict[n] += 1 
    else: 
      dict[n] = 1 
  return dict 
print(char_frequency('google.com')) 

# output - {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

