"""
A mountain array is defined as an array that

    has at least 3 elements
    has an element with the largest value called "peak", with index k.
    The array elements strictly increase from the first element to A[k], and then strictly decrease from A[k + 1] to the last element of the array. Thus creating a "mountain" of numbers.

That is, given A[0]<...<A[k-1]<A[k]>A[k+1]>...>A[n-1], we need to find the index k. Note that the peak element is neither the first nor the lastIndex of the array.

Find the index of the peak element. Assume there is only one peak element.

Input: 0 1 2 3 2 1 0

Output: 3

Explanation: The largest element is 3, and its index is 3.
"""

def find_peak_element(arr: list[int]) -> int:
    peak_index = -1
    left_ptr, right_ptr = 0, len(arr) - 1
    while left_ptr <= right_ptr:
        mid = (left_ptr + right_ptr) // 2
        if arr[mid] <= arr[mid + 1] and mid < len(arr) - 1:
            left_ptr = mid + 1

        else:
            peak_index = mid
            right_ptr = mid - 1

    return peak_index


if __name__ == "__main__":
    mountain = [int(num) for num in input("enter a mountain of numbers: ").split()]
    peak_element = find_peak_element(mountain)
    print(peak_element)