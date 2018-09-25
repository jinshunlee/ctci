# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

# Time O(n)
# Space O(n) - creates new string


def strCompression(string):
    i = 0
    count = 1
    newstr = []

    while i < len(string):
        if i + 1 == len(string) or string[i] != string[i + 1]:
            newstr.append(string[i] + str(count))
            count = 1
        else:
            count += 1
        i += 1
    return min("".join(newstr), string, key=len)


if __name__ == "__main__":
    print(strCompression("aabcccccaaa"))
    print(strCompression("abcdef"))
