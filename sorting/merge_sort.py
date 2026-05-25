"""
The idea of a merge sort is divide and conquer: We divide the array into two almost equally, sort them (usually another merge sort), and merge the two sorted lists into one.
To merge the two sorted lists, have two pointers pointing towards the bottom of the two lists, and in each step,
add the smaller element from those two into the list and move the pointer of that item up by one until elements from both lists are fully added.
"""

def merge_sort(arr: list[int]):

    n = len(arr)
    if n == 1:
        return arr

    mid = n // 2

    left_sort = merge_sort(arr[:mid])
    right_sort = merge_sort(arr[mid:])

    sorted_result = []
    i, j, = 0, 0
    while i < mid or j < n - mid:
        if i == mid:
            sorted_result.append(right_sort[j])
            j += 1

        elif j == n - mid:
            sorted_result.append(left_sort[i])
            i += 1

        elif left_sort[i] <= right_sort[j]:
            sorted_result.append(left_sort[i])
            i += 1

        else:
            sorted_result.append(right_sort[j])
            j += 1

    return sorted_result


if __name__ == "__main__":
    unsorted = [int(num) for num in input().split()]
    sorted_arr = merge_sort(unsorted)
    print(sorted_arr)

