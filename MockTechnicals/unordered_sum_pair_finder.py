# return postions of numbers that sum to a target (positons are not the indexes but if you counted 0th indexs as 1 or 1st position)

def sum_pair_finder(numbers, target):
    if len(numbers) == 2:
        return [1, 2]
    
    l = 0
    r = len(numbers) - 1

    while l != r:
        sum_indexes = numbers[l] + numbers[r]
        if sum_indexes == target:
            return [l + 1, r + 1]
        if sum_indexes < target:
            l += 1
        if sum_indexes > target:
            r += 1 
    