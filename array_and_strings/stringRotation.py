# String Rotation:Assume you have a method isSubstringwhich checks if one word is a substring
# of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").

# Time O(s1 + s2) 
# Space O(s2)
def stringRotation(s1, s2):
  return len(s1) == len(s2) and s1 in s2 + s2

if __name__ == "__main__":
  print(stringRotation("waterbottle", "erbottlewat"))
  print(stringRotation("abc", "cab"))
  print(stringRotation("abc", "bca"))
  print(stringRotation("", ""))
