# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

# Time O(n) 
# Space O(n)
from collections import Counter

def palindromePermutation(str):
  characters = {}
  for char in str.replace(" ","").lower():
    if char in characters:
      characters[char] += 1
    else:
      characters[char] = 1
  oddChars = 0
  for occ in characters.values():
    if occ % 2 == 1:
      oddChars += 1
  return oddChars <= 1

def palindromePermutation2(str):
  occs = Counter(str.replace(" ", "").lower())
  return sum(occ % 2 for occ in occs.values()) <= 1

if __name__ == "__main__":
  print(palindromePermutation("aba"))
  print(palindromePermutation("abcaa"))
  print(palindromePermutation("AbcdaBcd"))
  print(palindromePermutation("abc dabc"))
  print(palindromePermutation("Tact Coa"))
  print(palindromePermutation2("aba"))
  print(palindromePermutation2("abcaa"))
  print(palindromePermutation2("AbcdaBcd"))
  print(palindromePermutation2("abc dabc"))
  print(palindromePermutation2("Tact Coa"))