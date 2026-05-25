# def minimumCost(arr):
#     sum = 0
#     while len(arr) > 1:
#         sum_val = 0
#         for i in range(len(arr) - 1, len(arr) - 3, -1):
#             sum_val += arr[i]
#             arr[i] = -1
#         sum += sum_val
#         arr[len(arr) - 2] = sum
#         arr.pop()
#     return sum

# print(minimumCost([25, 10, 20]))


import heapq

def minimizeCost(arr):
    # Create a min-heap from the array
    heapq.heapify(arr)
    total_cost = 0

    # Continue until only one element remains in the heap
    while len(arr) > 1:
        # Pop two smallest elements
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        
        # Calculate their sum and add to total cost
        current_sum = first + second
        total_cost += current_sum

        # Push the sum back into the heap
        heapq.heappush(arr, current_sum)
    
    return total_cost

# Example usage:
arr = [25, 10, 20]
print(minimizeCost(arr))  # Output: 85
