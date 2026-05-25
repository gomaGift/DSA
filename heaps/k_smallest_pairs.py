import heapq


def k_smallest_pairs(nums1, nums2, k):

    heapq.heapify(nums1)
    heapq.heapify(nums2)

    res = []
    u = v = None
    for i in range(k):
        if i == 0:
            u = heapq.heappop(nums1)
            v = heapq.heappop(nums2)

        elif nums1[0] <= v:
            u = heapq.heappop(nums1)
        else:
            v = heapq.heappop(nums2)

        res.append([u, v])



    return res



print(k_smallest_pairs([1, 1, 11], [2, 4, 5], 3))