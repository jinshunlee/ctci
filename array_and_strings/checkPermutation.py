# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.

# Using XOR operator to sum all all characters in the 2 strings, as order does not matter in XOR
# Time O(n)
# Space O(1)


def checkPermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        sum = 0
        for c1, c2 in zip(str1, str2):
            sum ^= ord(c1) ^ ord(c2)
        return sum == 0


if __name__ == "__main__":
    print(checkPermutation("ab", "ba"))
    print(checkPermutation("ab", "cd"))
    print(checkPermutation("abc", "cde"))
