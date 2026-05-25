"""
Selection Sort
The idea for this sorting algorithm is that during each cycle, we find the smallest item from the unsorted pile and add it to the sorted pile.

To find the smallest element in the unsorted pile, we have a temporary variable keeping track of the index to the smallest element. We then compare each element in the unsorted pile to that element,
updating the new index if necessary.

After all the elements have been compared, we swap the element with the smallest index with the first element of the unsorted pile. The element is now part of the sorted pile.

"""

def selection_sort(arr: list[int]) -> list[int]:

    for i in range(len(arr)):
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                arr[j], arr[min_index] = arr[min_index], arr[j]
                min_index = j

    return arr


if __name__ == "__main__":
    unsorted = [int(num) for num in input().split()]
    sorted_arr = selection_sort(unsorted)
    print(sorted_arr)