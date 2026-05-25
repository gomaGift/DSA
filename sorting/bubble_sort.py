"""
Bubble Sort
The idea of bubble sort is this: for each pass, we use a pointer to point at the first element of the list.
For each cycle, we compare it to the next element in the list and swap them if the current item is greater, then move the pointer by one until it reaches the end of the list.
We repeat this process until the list becomes sorted. The list is sorted if, during a pass, no swapping occurs.

Note that the largest element will always "float" to the top during each pass, like a bubble.
Therefore, for each pass, we only need to consider the interval excluding the last element of the previous interval, and the list is guaranteed to be sorted within n passes.

"""

def bubble_sort(arr: list[int]):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - 1, i, -1):
            if arr[j] <= arr[j - 1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swapped = True

        if not swapped:
            return arr

    return arr



if __name__ == "__main__":
    unsorted = [int(num) for num in input().split()]
    sorted_arr = bubble_sort(unsorted)
    print(sorted_arr)
