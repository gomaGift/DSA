"""
Given a string S having lowercase English letters, returns a string with no instances of three identical consecutive letters, obtained from S by deleting the minimum possible number of letters.

Example 1:
Input: eedaaad
Output: eedaad
Explanation:
One occurrence of the letter a is deleted.

Example 2:
Input: xxxtxxx
Output: xxtxx
Explanation:
Note that the letter x can occur more than three times in the returned string if the occurrences are not consecutive.

Example 3:
Input: uuuuxaaaaxum
Output: uuxaaxum
"""
from math import ceil, floor


def filter_string(s: str) -> str:
    if not s or len(s) < 3:
        return s

    print(ceil(0.0))
    print(floor(0.0))
    start = 0
    i = 0
    while i < len(s):
        start = i
        while i < len(s) - 1 and s[i] == s[i+1]:
            i +=1
        i+=1
        length = i - start

        if length >= 3:
            delete_chars = length // 3
            s = s[:i - delete_chars] + s[i:]

    return s


if __name__ == "__main__":
    res = filter_string("uuuuxaaaaxum")
    print(res)

