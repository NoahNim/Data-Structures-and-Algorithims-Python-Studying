def most_frequent_char(s):
    counter = {
        s[0]: 0
    }
    most_freq = s[0]
    for letter in s:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
    for l in counter:
        if counter[l] > counter[most_freq]:
            most_freq = l
    return most_freq
