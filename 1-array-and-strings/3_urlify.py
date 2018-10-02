# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)

# Takes in str as a list of characters as string are immutable in python
# Assumes there may be more excessive space at end for the given input
# Time O(n)
# Space O(n) - due to array slicing at end as it creates a new copy, O(1) otherwise


def urlify(str, length):
    new_length = len(str)
    for i in reversed(range(length)):
        if str[i] == ' ':
            str[new_length - 3: new_length] = "%20"
            new_length -= 3
        else:
            str[new_length - 1] = str[i]
            new_length -= 1
    return str[new_length:]  # trims excessive space at the front of the list


if __name__ == "__main__":
    print(urlify(list("abc def   "), 7))
    print(urlify(list("abc def              "), 7)),
    print(urlify(list('much ado about nothing      '), 22)),
    print(urlify(list("abc def     "), 7))
