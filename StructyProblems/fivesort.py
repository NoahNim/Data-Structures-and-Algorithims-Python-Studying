def five_sort(nums):
  x = 0
  y = len(nums) - 1
  
  while x < y:
    if nums[y] == 5:
      y -= 1
    elif nums[x] == 5:
      nums[x], nums[y] = nums[y], nums[x]
      x += 1
      y -= 1
    else:
      x += 1
  return nums