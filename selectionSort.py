def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Input from the user
arr = input("Enter the list of numbers separated by spaces: ").split()
arr = [int(x) for x in arr]

sorted_arr = selection_sort(arr)
print("Sorted list using Selection Sort:", sorted_arr)