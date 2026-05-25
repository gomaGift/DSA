
def append_result_to_k(k):
    result = []
    for i in range(k):
        result.append(str(i))
    return  result


def base_k_strings(n, k):
    if n == 0: return []
    if n == 1: return append_result_to_k(k)
    return [digit + bit_string for digit in base_k_strings(1, k) for bit_string in base_k_strings(n-1, k)]


print(base_k_strings(4, 3))
print(base_k_strings(2, 3))


def cache():
    cache = {}
