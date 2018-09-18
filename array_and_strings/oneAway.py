# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
# Note: You can't solve this problem using sets, because sets remove two important pieces of information: how many times a character appears, and in what order the characters are listed.

#pre condition: str1 == str2 length
def oneReplace(str1, str2): 
  count = 0
  for x, y in zip(str1, str2):
    if x != y:
      count += 1
  return count < 2

#pre condition: str1 is the shorter than str2 by 1
def oneDiff(str1, str2): 
  for i in range (0, len(str1)):
    if str1[i] != str2[i]:
      if str1[i] != str2[i + 1]:
        return False
  return True

# Time O(n)
# Space O(1)
def oneAway(str1, str2):
  if len(str1) == len(str2):
    return oneReplace(str1, str2)
  elif len(str1) + 1 == len(str2):
    return oneDiff(str1, str2)
  elif len(str1) == len(str2) + 1:
    return oneDiff(str2, str1)
  else:
    return False

if __name__ == "__main__":
  print(oneAway("pale", "ple"))
  print(oneAway("pales", "pale"))
  print(oneAway("pale", "bale"))
  print(oneAway("pale", "bake"))
  print(oneAway("abc", "bc"))
  print(oneAway("abcde", "abcd"))  # should return True
  print(oneAway("abde", "abcde"))  # should return True
  print(oneAway("a", "a"))  # should return True
  print(oneAway("abcdef", "abqdef"))  # should return True
  print(oneAway("abcdef", "abccef"))  # should return True
  print(oneAway("abcdef", "abcde"))  # should return True
  print(oneAway("aaa", "abc"))  # should return False
  print(oneAway("abcde", "abc"))  # should return False
  print(oneAway("abc", "abcde"))  # should return False
  print(oneAway("abc", "bcc"))  # should return False