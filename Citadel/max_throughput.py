import heapq
from typing import List


def maximize_throughput(links: List[int], tasks: List[int]) -> int:
    links.sort()
    tasks.sort()
    max_through_put = 0
    for i in range(len(links)):
        j = binary_search(links[i], i, len(tasks) - 1, tasks)
        max_through_put += tasks[j]
    return max_through_put


def binary_search(target, low, high, sub_array: List[int]):
    min_index = -1
    while low <= high:
        mid = (low + high)//2
        diff = target - sub_array[mid]
        if diff > 0:
            min_index = mid
            low = mid + 1
        elif diff < 0:
            high = mid - 1
        else:
            return mid
    return min_index


print(maximize_throughput([10,15], [10,11,15]))


def max_with_heap(links: List[int], tasks: List[int]):
    links_heap = heapq.heapify(links)
    tasks_heap = heapq.heapify(tasks)
    total_sum = 0
