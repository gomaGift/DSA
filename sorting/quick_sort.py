""""
Quick sort is a divide-and-conquer algorithm that sorts a list by partitioning it around a chosen element called the "pivot."
The main idea is to rearrange the list so that all elements less than the pivot come before it, and all elements greater than or equal to the pivot come after it. This process is called partitioning.

Here's how it works step by step:

Select a pivot element from the list (the choice can be arbitrary).
Rearrange the elements so that everything less than the pivot is on its left, and everything greater than or equal to the pivot is on its right.
The pivot is now in its final sorted position.
Recursively apply the same process to the sublists on the left and right of the pivot.
One common way to partition is to use two pointers: one starting just before the beginning of the interval, and one at the end.
Move the left pointer forward until you find an element greater than or equal to the pivot, and move the right pointer backward until you find an element less than or equal to the pivot.
If the pointers haven't crossed, swap these two elements and continue.
When the pointers meet or cross, swap the pivot into its correct position. This ensures that after partitioning, the pivot separates the list into two parts that can be sorted independently.
"""

def partition(arr: list[int], start, end) -> list[int]:
    if end - start <= 1:
        return arr

    left_ptr, right_ptr = start, end
    pivot = end

    while left_ptr < right_ptr:
        while arr[left_ptr] < arr[pivot] and left_ptr < right_ptr:
            left_ptr += 1

        while arr[right_ptr] > arr[pivot] and left_ptr < right_ptr:
            right_ptr -= 1

        arr[left_ptr], arr[right_ptr] = arr[right_ptr], arr[left_ptr]

    arr[left_ptr], arr[pivot] = arr[pivot], arr[left_ptr]

    partition(arr, start, left_ptr - 1)
    partition(arr, left_ptr + 1, end)

    return arr

def quick_sort(arr: list[int]):
    return partition(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    unsorted = [int(num) for num in input().split()]
    sorted_arr = quick_sort(unsorted)
    print(sorted_arr)



