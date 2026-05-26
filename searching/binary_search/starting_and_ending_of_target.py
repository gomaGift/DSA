"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

Constraints:

    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
    nums is a non-decreasing array.
    -10^9 <= target <= 10^9
"""
def search_left(arr: list[int], target: int) -> int:
    start = -1
    left_ptr, right_ptr = 0, len(arr) - 1

    while left_ptr <= right_ptr:
        mid = (left_ptr + right_ptr) // 2
        if arr[mid] == target:
            start = mid
            right_ptr = mid - 1

        elif arr[mid] > target:
            right_ptr = mid - 1
        else:
            left_ptr = mid + 1

    return  start


def search_right(arr: list[int], target: int) -> int:
    end = - 1
    left_ptr, right_ptr = 0, len(arr) - 1
    while left_ptr <= right_ptr:
        mid = (left_ptr + right_ptr) // 2

        if arr[mid] == target:
            end = mid
            left_ptr = mid + 1
        elif arr[mid] < target:
            left_ptr = mid + 1
        else:
            right_ptr = mid -1

    return  end


def find_starting_and_ending_of_target(arr: list[int], target: int) -> list[int]:

    start = search_left(arr, target)
    end = search_right(arr, target)

    return [start, end]


if __name__ == "__main__":
    arr = [int(num) for num in input('enter search array: ').split()]
    target = int(input("enter target num: "))
    res = find_starting_and_ending_of_target(arr, target)
    print(res)

