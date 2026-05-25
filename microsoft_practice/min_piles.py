from collections import Counter


def min_steps(nums: list[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    nums.sort()
    pivot = None
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] >= nums[i - 1]:
            pivot = i
            break

    if not pivot:
        return 0

    steps = 0
    while pivot > 0:
        if nums[pivot] > nums[pivot - 1]:
            for i in range(pivot, len(nums)):
                steps += 1

        pivot -= 1

    return steps


if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    res = min_steps(nums)
    print(res)




def min_steps(arr):
    cnt = Counter(arr)
    nums = sorted(cnt.keys(), reverse=True)
    print(nums[:-1])
    k, ans = 0, 0
    for x in nums[:-1]:
        k += cnt[x]
        ans += k
    return ans
# smart dog

if __name__ == "__main__":
    res = min_steps([1,1,2,2,5,5])
    print(res)