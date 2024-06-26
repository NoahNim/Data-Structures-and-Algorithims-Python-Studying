def cat_dog(s):
    count_cat = 0
    count_dog = 0

    for i in range(0, len(s) - 2):
        if s[i : i + 3] == "cat":
            count_cat += 1
        elif s[i : i + 3] == "dog":
            count_dog += 1
    if count_cat == count_dog:
        return True
    return False
