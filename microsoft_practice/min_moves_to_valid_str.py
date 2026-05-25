"""
🧩 Problem Statement — Minimum Moves to Make String Valid
You are given a string s consisting only of lowercase English letters.
In one move, you can remove any one character from the string.
Your task is to determine the minimum number of moves required so that the resulting string does not contain any three identical consecutive characters.
Formally, after all moves, there should be no substring of the form xxx, where all three characters are equal.
💡 Example 1
Input:
s = "baaa"

Output:1

Explanation:
There are three consecutive 'a's.
Removing one 'a' gives "baa", which has no triple repeats.

💡 Example 2
Input: s = "baaabbaabbba"
Output: 2

Explanation:
We have "aaa" and "bbb" groups — each of size 3.
We must remove one from each → total 2 moves.

"""


def minMovesToValidString(s: str) -> int:
    if not s or len(s) < 3:
        return 0

    moves = 0

    start = 0
    i  = 0
    while i < len(s):
        start = i
        while i < len(s) - 1 and s[i] == s[i+1]:
             i+= 1

        i+=1

        length = i - start
        if length >= 3:
            moves += length // 3


    return moves
