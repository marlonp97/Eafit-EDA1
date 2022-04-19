# Punto 2

# Camilo Villa Tamayo
# Miguel Angel Sarmiento Aguiar
# Marlon Perez Rios

def Suma_grupo1(nums, target):
  return Suma_grupo(0, nums, target)

def Suma_grupo(start, nums, target):
  if start >= len(nums):
    return target == 0
  else:
    return (Suma_grupo(start + 1, nums, target - nums[start]) or Suma_grupo(start + 1, nums, target))

print(Suma_grupo1([2, 4, 8],14))
