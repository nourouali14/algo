def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be compared

        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key at its correct position in the sorted sequence
        arr[j + 1] = key

# Example usage:
my_array = [12, 11, 13, 5, 6]
insertion_sort(my_array)
print("Sorted array:", my_array)
