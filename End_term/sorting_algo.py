# Selection sort - sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list. 

def insertionSort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j] :
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key

def selection_sort(arr):
  n = len(arr)
  for i in range(n-1):
    min_idx = i
    for j in range(i+1,n):
      if arr[j] < arr[min_idx]:
        min_idx = j

    arr[min_idx], arr[i] = arr[i], arr[min_idx]

  return arr

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


print("=================\n")
finalList = []
l1 = [4,3,5,6,2,1]
print(f"List: {l1}")


# finalList = selection_sort(l1)
# print(f"Final sorted list: {finalList}")




print("\n=================")
