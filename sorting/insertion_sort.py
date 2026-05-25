"""
Insertion Sort
The idea of an insertion sort is this: initially, only the first item is considered sorted.
Then, for each item in the sequence, we "insert" that item into the sorted list by swapping it left while current_item < previous_item.

Imagine you are sorting a hand of cards.
 What people usually do is maintain a pile of sorted cards and inserting from the unsorted pile into the sorted pile in the correct position. This algorithm is based on this idea
"""

def insertion_sort(arr: list[int]):

    for i in range(1, len(arr)):
        index = i
        while index > 0 and arr[index] <= arr[index - 1]:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1

    return  arr


if __name__ == "__main__":
    unsorted = [int(num) for num in input().split()]
    sorted_arr = insertion_sort(unsorted)
    print(sorted_arr)