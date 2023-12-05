def max_value(nums):
    max = nums[0]
    for n in nums:
        if n > max:
            max = n
    return max
