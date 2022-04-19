# Miguel Angel Sarmiento Aguiar
# Marlon Perez Rios

# Punto 2.1.1

def countEvens(nums):
  n = 0
  for  i in range(len(nums)):
    if (nums[i]%2 == 0):
      n = n+1
  return n

countEvens([2, 1, 2, 3, 4])

# Punto 2.1.2

def lucky13(nums):
  for i in range(len(nums)):
    if ((nums[i] == 1) or (nums[i] == 3)):
      return False
  return True

lucky13([0, 1, 4])

# Punto 2.1.3

def isEverywhere(nums, val):
  for i in range(len(nums)-1):
    if ((nums[i] != val) and (nums[i+1] != val)):
      return False
  return True

isEverywhere([1, 2, 1, 2, 3, 2, 5], 2)

# Punto 2.1.4

def modThree(nums):
  for i in range(len(nums)-2):
    if ((nums[i]%2 == 0) and (nums[i+1]%2 == 0) and (nums[i+2]%2 == 0)):
      return True
    elif ((nums[i]%2 == 1) and (nums[i+1]%2 == 1) and (nums[i+2]%2 == 1)):
      return True
  return False

modThree([9, 7, 2, 9, 2, 2, 6])

# Punto 2.1.5

def tripleUp(nums):
  for i in range(len(nums)-2):
    if ((nums[i+1] == nums[i]+1) and (nums[i+2] == nums[i]+2)):
      return True
  return False

tripleUp([10, 9, 8, -100, -99, -98, 100])

# Punto 2.2.1

def linearIn(outer, inner):
  n = 0
  for i in range(len(inner)):
    for j in range(len(outer)):
      if (inner[i] == outer[j]):
        n = n+1
        break
  return n == len(inner)

linearIn([-1, 0, 3, 3, 3, 10, 12], [-1, 0, 3, 12])

# Punto 2.2.2

def seriesUp(n):
  array = [None]*(n*(n+1)//2)
  num = 0
  for i in range(n):
    for j in range(i+1):
      array[num] = j+1
      num = num+1
  return array

seriesUp(6)

# Punto 2.2.3

def fix34(nums):
  n = 0
  for i in range(len(nums)):
    if (nums[i] == 3):
      for j in range(n, len(nums)):
        if (nums[j] == 4):
          n = j
          aux = nums[j]
          nums[n] = nums[i+1]
          nums[i+1] = aux
          break
  return nums

fix34([3, 1, 1, 3, 4, 4])

# Punto 2.2.4

def maxSpan(nums):
  cont = 0
  cont2 = 0
  for i in range(len(nums)):
    for j in range(len(nums)-1, 0, -1):
      if (nums[i] == nums[j]):
        cont = (j-i)+1
        if (cont > cont2):
          cont2 = cont
          cont = 0
  return cont2

maxSpan([1, 4, 2, 1, 4, 4, 4])

# Punto 2.2.5

def squareUp(n):
  array = [0]*(n*n)
  p = 0
  for i in range(n):
    p = n*(i+1)-1
    for j in range(i+1):
      array[p] = j+1
      p = p-1
  return array

squareUp(4)
