def add_front_of_beginning(x, L):
    return [x + digit for digit in L]


def bit_string(n) :
    if n == 0: return []
    if n == 1: return  ['0', '1']
    return add_front_of_beginning("0", bit_string(n-1)) + add_front_of_beginning ("1", bit_string(n-1))

print(bit_string(4))

def bit_string_alternative(n):
    if n == 0:
        return []
    if n ==1:
        return ['0', '1']
    return [digit + bit for digit in bit_string_alternative(1) for bit in bit_string_alternative(n-1)]

print( bit_string_alternative(4))

