
"""
📌 Problem Statement
You are given an integer array arr of length n (1 ≤ n ≤ 10^5).
Count the number of index pairs (i, j) such that:
  - 0 ≤ i < j < n
  - arr[i] == arr[j]
  - arr[i] == sum(arr[i+1 ... j-1])

Return this count as an integer.

⚙️ Constraints
 ->  1 ≤ n ≤ 10^5
 -> -10^4 ≤ arr[k] ≤ 10^4
Time Complexity: O(n log n) or better (since brute-force O(n²) would time out).
Memory limit: ~512 MB.
"""
from typing import List


def subarray_sum_with_equal_endpoint(arr: List[int]):
    count = 0
    prefix_sum = []
    prefix_sum.append(arr[0])
    endpoints_map = {}
    endpoints_map[arr[0], prefix_sum[-1]] = 0
    indices = []

    for i in range(1, len(arr)):
        prefix_sum.append(prefix_sum[-1] + arr[i])
        endpoints_map[arr[i], prefix_sum[i]] = i

    for j in range(1, len(arr)):
        if (arr[j], prefix_sum[j-1] - arr[j]) in endpoints_map:
             count += 1
             i = endpoints_map.get((arr[j], prefix_sum[j-1] - arr[j]))
             indices.append((i, j))
    print(indices)
    return count





print(subarray_sum_with_equal_endpoint([1,1,1,1,1]))