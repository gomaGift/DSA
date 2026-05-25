from typing import List


def majorityElement(arr):
    #     arr.sort()
    #     return arr[len(arr)//2]

    # nums.sort()
    # val = nums[0]
    # max_count_num = val
    # max_count = count = 1

    # for i in range(1, len(nums)):
    #     if nums[i] != val:
    #          max_count = max(count, max_count)
    #          if max_count == count:
    #             max_count_num = val

    #          val = nums[i]
    #          count = 1

    #     else:
    #         count += 1
    # if max_count < count:
    #     return val
    # return max_count_num


    count = 0
    candidate = None

    for num in arr:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate

print(majorityElement([2, 3, 3]))