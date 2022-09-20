def string_times(str, n):
  return n*str

def front_times(str, n):
  return n*str[:3]
  
def string_bits(str):
  return str[::2]
  
def string_splosion(str):
  result = ""
  for i in range(len(str)+1):
    result += str[:i]
  return result

def last2(str):
  count = 0
  last2 = str[-2:]
  for i in range(len(str)-2):
    if str[i:i+2] == last2:
      count += 1
  return count

def array_count9(nums):
  count = 0
  for i in nums:
    if i == 9:
      count += 1
  return count

def array_front9(nums):
  for i in nums[:4]:
    if i == 9:
      return True
  return False

def array123(nums):
  for i in range(len(nums)-2):
    if nums[i:i+3] == [1,2,3]:
      return True
  return False

def string_match(a, b):
  minilength = min(len(a),len(b))
  count = 0
  for i in range(minilength-1):
    if a[i:i+2] == b[i:i+2]:
      count += 1
  return count
