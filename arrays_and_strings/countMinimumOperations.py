from bisect import bisect_left

def countMinimumOperations(price, query):
    # Step 1: Sort the price array and compute prefix sums
    price.sort()
    n = len(price)
    
    # Calculate prefix sums
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + price[i - 1]
    
    result = []
    
    # Step 2: Process each query using the sorted array and prefix sums
    for target in query:
        # Find the position where elements start to be greater than or equal to the target
        k = bisect_left(price, target)

        # Calculate the sum of operations for elements less than target
        left_cost = k * target - prefix[k]
        
        # Calculate the sum of operations for elements greater than or equal to target
        right_cost = (prefix[n] - prefix[k]) - (n - k) * target
        
        # Total cost for this query
        result.append(left_cost + right_cost)
    
    return result

# Example usage:
price = [2, 3, 1]
query = [3, 2, 1, 5]
print(countMinimumOperations(price, query))  # Output: [3, 2, 3, 9]
