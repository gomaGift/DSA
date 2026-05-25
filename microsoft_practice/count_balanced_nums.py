def countBalancedNumbers(p):
    n = len(p)
    pos = [0] * (n + 1)

    # record the position of each number
    for i, num in enumerate(p):
        print(i, num)
        pos[num] = i
    print(pos)
    result = []
    min_pos = float('inf')
    max_pos = float('-inf')

    # iterate from 1 to n
    for k in range(1, n + 1):
        min_pos = min(min_pos, pos[k])
        max_pos = max(max_pos, pos[k])
        if (max_pos - min_pos + 1) == k:
            result.append('1')
        else:
            result.append('0')

    return ''.join(result)
print(countBalancedNumbers([4,1,3,2]))