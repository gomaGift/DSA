"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8] Output: 2

Example 2:

Input: nums = [3,3,7,7,10,11,11] Output: 10

Constraints:

    1 <= nums.length <= 105
    0 <= nums[i] <= 105
"""

def to_the_left(arr: list[int], index: int) -> bool:
    if index % 2:
        print(f"index {index}")
        return arr[index] != arr[index - 1]

    else:
        return arr[index] != arr[index + 1]


def find_single_non_dup_number(arr: list[int]) -> int:

    unique = -1

    left_ptr, right_ptr = 0, len(arr)  - 1

    while left_ptr <= right_ptr:
        mid = (left_ptr + right_ptr) // 2
        if to_the_left(arr, mid):
            unique = arr[mid]
            right_ptr = mid - 1
        else:
            left_ptr = mid + 1
    return unique

if __name__ == "__main__":
    dups = [int(num) for num in input("enter dups with unique: ").split(",")]
    print(dups)
    non_dup = find_single_non_dup_number(dups)
    print(non_dup)
