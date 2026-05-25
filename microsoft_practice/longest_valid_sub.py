"""
Given a string str containing only a and b, find the longest substring of str such that it does not contain more than two contiguous occurrences of a and b.

Example 1:
Input: aabbaaaaabb
Output: aabbaa
Example 2:
Input: aabbaabbaabbaaa
Output: aabbaabbaabbaa
"""

from itertools import groupby



def longest_valid_string(s: str) -> str:
    # WRITE YOUR BRILLIANT CODE HERE
    start = 0
    a_count = b_count = 0
    valid = ""

    for i, ch in enumerate(s):
        if ch == 'a':
            b_count = 0
            a_count += 1
            if a_count > 2:
                a_count = 1
                valid = max(valid, s[start:i], key=len)
                start = i
        elif ch == 'b':
            a_count = 0
            b_count += 1
            if b_count > 2:
                b_count = 1
                valid = max(valid, s[start:i], key=len)
                start = i

    return valid



def longest_valid_string(s: str) -> str:
    loc = ""
    ans = ""
    print(groupby(s))
    for c, g in groupby(s):
        glen = len(list(g))
        ans = max([ans, loc + c * min(glen, 2)], key=len)
        if glen > 2:
            loc = c * 2
        else:
            loc += c * glen
    return ans

if __name__ == "__main__":
    res = longest_valid_string("aabbababbaabaababbababaababbabababababaaababababbabaaabbbaabbabbababababaabba")
    print(res)


