"""
A sorted array of unique integers was rotated at an unknown pivot. For example, [10, 20, 30, 40, 50] becomes [30, 40, 50, 10, 20]. Find the index of the minimum element in this array.

Input: [30, 40, 50, 10, 20]

Output: 3

Explanation: The smallest element is 10, and its index is 3.

Input: [3, 5, 7, 11, 13, 17, 19, 2]

Output: 7

Explanation: The smallest element is 2, and its index is 7.

"""

"""
At first glance, it seems that there's no way to do it in less than linear time because the array is not sorted.

But remember binary search can work beyond sorted arrays, as long as there is a binary decision we can use to shrink the search range.

Let's draw a figure to see if there's any pattern. If we plot the numbers against their index, we get:
"""

def find_min_in_rotated_array(arr: list[int]):
    min_index = -1
    left_ptr, right_ptr = 0, len(arr) -1

    while left_ptr <= right_ptr:
        mid = (left_ptr + right_ptr) // 2

        if arr[mid] <= arr[-1]:
            right_ptr = mid - 1
            min_index = mid

        else:
            left_ptr = mid + 1

    return min_index


if __name__ == "__main__":
    rotated_arr = [int(num) for num in input("enter rotated arr: ").split()]
    min_in_rotated = find_min_in_rotated_array(rotated_arr)
    print(min_in_rotated)


