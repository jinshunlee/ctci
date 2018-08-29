# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

# Questions to ask interviewer:
# Is the String ASCII or Unicode 
# - ASCII has 128 characters
# - Unicode has 2^16 65536 characters
# we can do a check if len(str) > no. of possible characters in either ascii or unicode
# return false

# Assuming we cannot use additional data structure:
# Time O(n^2) 
# Space O(1)
def isUnique(str):
  for i in range(0, len(str) - 1):
    for j in range(i + 1, len(str)):
      if str[i] == str[j]:
        return False
  return True

# With auxilary data structure allowed:
def isUniqueWithSet(str):
  return len(set(str)) == len(str)

# If we are allowed to modify the input string, we may consider sorting the string
# then compare adjacent characters of the string for duplicates in linear time
# Time O(n log n)
# Space O(1) -> Using Heap Sort -> no auxilary space used

if __name__ == "__main__":
  print(isUnique("abcd"))
  print(isUnique("abcda"))
  print(isUniqueWithSet("abcd"))
  print(isUniqueWithSet("abcda"))




