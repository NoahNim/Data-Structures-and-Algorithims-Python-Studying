def sum78(nums):
    total_sum = 0
    in_section = False

    for n in nums:
        if n == 7:
            in_section = True
        elif n == 8 and in_section == True:
            in_section = False
            continue
        if in_section == False:
            total_sum += n
    return total_sum