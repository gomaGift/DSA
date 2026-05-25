"""
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1

Constraints: 1 <= bad <= n <= 231 - 1
"""


def first_product_bad_version(n, bad_product: int):

    low_version = 1
    highest_version = n
    first_bad_product = -1
    while low_version <= highest_version:
        mid_version = (low_version + highest_version) // 2

        if mid_version >= bad_product:
            highest_version = mid_version - 1
            first_bad_product = mid_version

        else:
            low_version = mid_version + 1

    return  first_bad_product



if __name__ == "__main__":
   n = int(input("enter the number of versions: "))
   bad_product = int(input("enter the version of the bad priduct: "))
   first_bad = first_product_bad_version(n, bad_product)
   print(first_bad)
