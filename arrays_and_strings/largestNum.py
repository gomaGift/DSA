def largestNum(s):
    ptr1 = 0
    ptr2 = 1

    while ptr2 < len(s):
        num1 = int(s[ptr1])
        num2 = int(s[ptr2])

        if num2 % 2 == 0 and num1 % 2 == 0:
            num2 > num1 # swap
            temp = num1
            s[ptr1] = num2
            s[ptr2] = num1
        

        ptr1 += 1
        ptr2 += 1
    return




