# Consider a scenario where you are tasked with finding unique combinations of letters within any given sequence, particularly focusing on combinations that span three characters without any repetition.
 
# You will be given a string, and your objective is to count how many distinct 3-letter combinations can be found within it.
# It's important to note that each character sequence, or substring, should be evaluated as its own entity, meaning if the same combination appears more than once, each occurrence is counted separately.
 
# A 'good' substring is defined as a 3-character sequence within the string that does not include any repeated characters.
 
# For instance:
# Input: s = "xyzzaz"
# Output: 1
# In this example, "xyz" is the only 'good' substring among the four possible substrings ('xyz', 'yzz', 'zza', 'zaz').
 
# Another Example:
# Input: s = "aababcabc"
# Output: 4
# Here, the 'good' substrings are 'abc', 'bca', 'cab', and again 'abc', making a total of four distinct occurrences although 'abc' appears twice.
 
# Constraints:
# - The input string s will have a length ranging from 1 to 100 characters.
# - The string will only consist of lowercase English letters.

def countUniqueTrios(s):
    count = 0

    for i in range(0, len(s) - 2):
        curr_set = set(s[i:i+3])
        if len(curr_set) == 3:
            count += 1
    return count

