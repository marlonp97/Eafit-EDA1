# Camilo Villa Tamayo
# Miguel Angel Sarmiento Aguiar
# Marlon Perez Rios

# Punto 2.1.1

def factorial(n):
  if (n == 1):
    return 1
  else:
    return n*factorial(n-1)

factorial(5)

# Punto 2.1.2

def fibonacci(n):
  if (n == 0):
    return 0
  elif (n == 1):
    return 1;
  return fibonacci(n-1) + fibonacci(n-2)

fibonacci(6)

# Punto 2.1.3

def bunnyEars(bunnies):
  if (bunnies == 0):
    return 0;
  else:
    return 2 + bunnyEars(bunnies-1)

bunnyEars(10)

# Punto 2.1.4

def triangle(rows):
  if (rows == 0):
    return 0
  else:
    return rows + triangle(rows-1)

triangle(4)

# Punto 2.1.5

def sumDigits(n):
  if (n == 0):
    return 0
  else:
    return n%10 + sumDigits(n//10)

sumDigits(126)

# Punto 2.2.1

def splitArray(nums):
  return splitArrayAux(0, nums, 0, 0)

def splitArrayAux(start, nums, g1, g2):
  if (start >= len(nums)):
    return g1 == g2
  elif (splitArrayAux(start+1, nums, g1 + nums[start], g2)):
    return True
  elif (splitArrayAux(start+1, nums, g1, g2 + nums[start])):
    return True
  else:
    return False

splitArray([2, 5, 3])

# Punto 2.2.2

def splitOdd10(nums):
  return splitOdd10Aux(0, nums, 0, 0)

def splitOdd10Aux(start, nums, mult, imp):
  if (start >= len(nums)):
    return (mult%10 == 0) and (imp%2 == 1)
  elif (splitOdd10Aux(start+1, nums, mult+nums[start], imp)):
    return True
  elif (splitOdd10Aux(start+1, nums, mult, imp+nums[start])):
    return True
  else:
    return False

splitOdd10([5, 5, 6, 1])

# Punto 2.2.3

def split53(nums):
  return split53Aux(0, nums, 0, 0)

def split53Aux(start, nums, n5, n3):
  if (start >= len(nums)):
    return n5 == n3
  elif (nums[start]%5 == 0):
    return split53Aux(start+1, nums, n5+nums[start], n3)
  elif (nums[start]%3 == 0):
    return split53Aux(start+1, nums, n5, n3+nums[start])
  elif (split53Aux(start+1, nums, n5+nums[start], n3)):
    return True
  elif (split53Aux(start+1, nums, n5, n3+nums[start])):
    return True
  else:
    return False

split53([2, 4, 2])

# Punto 2.2.4

def groupSumClump(start, nums, target):
  if (start >= len(nums)):
    return target == 0
  sum = nums[start]
  while ((start < len(nums)-1) and (nums[start+1] == nums[start])):
    sum = sum+nums[start+1]
    start = start+1
  return groupSumClump(start+1, nums, target-sum) or groupSumClump(start+1, nums, target)

groupSumClump(0, [2, 4, 8], 10)

# Punto 2.2.5

def groupSum6(start, nums, target):
  if (start >= len(nums)):
    return target == 0
  elif (nums[start] == 6):
    return groupSum6(start+1, nums, target-nums[start])
  else:
    return groupSum6(start+1, nums, target-nums[start]) or groupSum6(start+1, nums, target)

groupSum6(0, [5, 6, 2], 8)
