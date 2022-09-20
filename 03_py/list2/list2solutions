def count_evens(nums):
  count = 0
  for i in nums:
    if i % 2 == 0:
      count += 1
  return count
  
def big_diff(nums):
  mi = nums[0]
  ma = nums[0]
  for i in nums:
    mi = min(mi,i)
    ma = max(ma,i)
  return ma-mi
  
def centered_average(nums):
  mi = nums[0]
  ma = nums[0]
  al = 0
  for i in nums:
    mi = min(mi,i)
    ma = max(ma,i)
    al += i
  return (al - mi - ma) / (len(nums)-2)
  
def sum13(nums):
  sum = 0
  i = 0
  while i < len(nums):
    if nums[i] != 13:
      sum += nums[i]
      i -= 1
    i += 2
  return sum
  
def sum67(nums):
  sum = 0
  sixfound = False
  for i in nums:
    if i == 6:
      sixfound = True
    if sixfound == False:
      sum += i
    else:
      if i == 7:
        sixfound = False
  return sum
  
def has22(nums):
  found = False;
  for i in range(len(nums)-1):
    if (nums[i] == 2 and nums[i+1] == 2):
      found = True
  return found
  
