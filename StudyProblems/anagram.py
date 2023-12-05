def char_count(s):
    count = {}

    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1

    return count


def anagrams(s1, s2):
    return char_count(s) == char_count(t)
    # l2 = list(s2)

    # if len(s2) > len(s1) or len(s2) < len(s1):
    #     return False

    # for letter in s1:
    #     if letter in l2:
    #         l2.remove(letter)

    # if len(l2) == 0:
    #     return True
    # else:
    #     return False
