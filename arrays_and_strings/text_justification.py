"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
"""


def text_justification(words: list[str], max_width: int) -> list[str]:
    result = []
    current_length = 0
    current_line = []
    for word in words:
        if current_length + len(current_line) + len(word) > max_width:
            spaces_to_add = max_width - current_length
            for i in range(spaces_to_add):
                current_line[i%(len(current_line) - 1 or 1)] += ' '
            result.append(''.join(current_line))
            current_line, current_length = [], 0
        current_line.append(word)
        current_length += len(word)

    # left justify the last word
    result.append(' '.join(current_line).ljust(max_width))

    return result


print(text_justification(["This", "is", "an", "example", "of", "text", "justification."]
, 16))