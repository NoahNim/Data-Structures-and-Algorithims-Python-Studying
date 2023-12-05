def intersection(a, b):
    intersection_list = []
    list_set = set(a)
    for ele in b:
        if ele in list_set:
            intersection_list.append(ele)
    return intersection_list
