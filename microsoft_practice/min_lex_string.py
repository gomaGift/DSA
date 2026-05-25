# def smallest_string(s: str) -> str:
#     # WRITE YOUR BRILLIANT CODE HERE
#     max_char, index = s[0], 0
#     for i in range(1, len(s)):
#                 if s[i] > max_char:
#                     max_char = s[i]
#                     index = i
#     try:
#               return s[:index] + s[index+1:]
#     except:
#                 if index == 0:
#                     return s[1:]
#                 return s[:index]



def smallest_string(s: str) -> str:
    i = 0
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            break
    return s[:i] + s[i + 1 :]



print(smallest_string("abdc"))