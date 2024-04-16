def findSubstringStart(haystack, needle):
    #######################
    # create two pointer varuables len_needle = len(needle) len_haystack = len(haystack)
    # if len(needle) is empty, then return 0
    # loop through range of 0, len_heystack - len_needle + 1
    #   substring = haystack[i:i+len_needle]
    #   if substring == needle return i
    # return -1
    #######################
    
    # check if needle is empty
    if not needle:
        return 0
    # length of needle and haystack    
    len_needle = len(needle)
    len_haystack = len(haystack)
    # iterate through haystack minus needle length plus 1
    for i in range(0, len_haystack - len_needle + 1):
        # create substring from current index
        substring = haystack[i:i + len_needle]
        # check if substring equals needle
        if substring == needle:
            return i
    # return -1 if no needle found
    return -1