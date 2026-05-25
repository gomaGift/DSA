def merge(nums1: list[int], m: int, nums2: list[int], n: int):
  # [1,2,3, 0, 0, 0]  [2,5,6]
  j = n - 1
  i =  m - 1
  k = m + n - 1
  while j >= 0:
      if i >= 0 and nums1[i] > nums2[j]:
          nums1[k] = nums1[i]
          i -= 1
      else:
          nums1[k] = nums2[j]
          j-= 1
      k-=1
  return nums1

print(merge([1, 3, 4, 0, 0, 0], 3, [2, 5, 7], 3))