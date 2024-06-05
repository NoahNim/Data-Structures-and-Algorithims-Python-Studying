# Determine if two provided words are anagrams of each other.
# An anagram is defined as a word obtained by rearranging the letters of another word, using all the original letters exactly once.
# For this verification, input consists of two strings: 's' representing the first word, and 't' for the second word.
# The goal is to return true if 't' is an anagram of 's', otherwise, return false.
 
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
 
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
 
# Constraints:
# - The length of both strings 's' and 't' will be in the range of 1 to 50,000.
# - Both strings will contain only lowercase English letters.

def is_anagram(s, t):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for char in t:
        if char in count:
            count[char] -= 1
        else:
            return False
    for value in count.values():
        if value != 0:
            return False
    return True