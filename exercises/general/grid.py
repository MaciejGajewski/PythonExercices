# Exercise:
# Given a string with "words" (something which is divided by one or more whitespaces).
# Return a string with each "word" reversed  retaining the same amount of whitespaces between them.
# Example:
# input: "abc def   lll"
# output: "cba fed   lll"
from collections import deque
import re


def reverse_words_orig(input_str: str) -> str:
    out = ""
    for token in input_str.split(" "):
        # print("Token:" + token)
        # print(token[::-1])

        out = out + token[::-1] + " "

    return out.rstrip()


def reverse_words_my(input_str: str) -> str:
    out = ""
    reversed_word = deque([])

    for idx, char in enumerate(input_str):
        if char == " ":
            reversed_word.append(char)
        else:
            reversed_word.appendleft(char)

        if char == " " or idx == len(input_str)-1:
            out += "".join(reversed_word)
            reversed_word.clear()

    return out


def reverse_words_find(string):
    words = string.split()  # split the string into words
    reversed_words = [word[::-1] for word in words]  # reverse each word
    # build the result string by alternating reversed words and spaces
    result = ''
    for i, word in enumerate(reversed_words):
        result += word
        if i != len(reversed_words) - 1:
            # add the same number of spaces as in the original string
            result += string[string.find(words[i])+len(words[i]):string.find(words[i+1])]
    return result


def reverse_words(string):
    return re.sub(r'\w+', lambda m: m.group(0)[::-1], string)


print(reverse_words("abc abc abc def   lll"))
print(len(reverse_words("abc def   lll")))
print(len("cba fed   lll"))

assert reverse_words("abc def   lll") == "cba fed   lll"
assert reverse_words("aaa") == "aaa"
assert reverse_words("") == ""

print("All done")
