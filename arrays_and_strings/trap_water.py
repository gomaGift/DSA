"""
        Given n non-negative integers representing an elevation map where the width of each bar is 1,
         compute how much water it can trap after raining.
"""
def trap_raining_water(height: list[int]) -> int:
    n = len(height)
    left = [0] * n
    right = [0] * n

    left[0] = height[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], height[i])

    right[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(height[i],right[i + 1])

    water_trapped = 0
    for i, bar in enumerate(height):
        water_trapped += min(left[i], right[i]) - bar
    return water_trapped



def trap_raining_waters(height: list[int]) -> int:
    left_max = height[0]
    water_trapped = 0
    for i in range(1, len(height)):
        left_max = max(left_max, height[i - 1])
        right_max = max(height[i:])
        water_trapped += max(0, min(left_max, right_max) - height[i])

    return water_trapped

print(trap_raining_water([4,2,0,3,2,5]))
print(trap_raining_waters([4,2,0,3,2,5]))

