def uncompress(s):
    new_str = ""
    a = 0
    b = 1
    digits = ""
    numsHash = {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9"
    }

    while a < len(s):
        if s[a] in numsHash:
            digits += s[a]
        elif s[a] not in numsHash:
            digits = ""
        if s[a] in numsHash and s[b] not in numsHash:
            result_string = s[b] * int(digits)
            new_str += result_string
        if b != len(s) - 1:
            b += 1
        a += 1
    return new_str
