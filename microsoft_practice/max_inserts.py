def max_inserts(s: str) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    count = 0
    res = ""

    i = 0

    while len(s) < 2:
        ch = s[i]
        if ch == 'a':
            res += ch

        elif not res:
            res += "aa" + ch
            count += 2
        else:
            res += 'a' + ch
            count += 1
        i += 1
    print(res)
    #
    # while i < len(s):
    #     if s[i] != 'a':
    #         if res[-1] == 'a':
    #             res += 'a' + s[i]
    #             count += 1
    #         else:
    #             res += 'aa' + s[i]
    #             count += 2
    #     elif res[-1] == res[-2] == s[i]:
    #         return -1
    #     else:
    #         res += s[i]
    #     i += 1

    return count


if __name__ == "__main__":
    res = max_inserts("dog")
    print(res)
