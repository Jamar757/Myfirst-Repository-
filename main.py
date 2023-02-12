def factorial(j):
  if j == 0:
    return 1
  else:
    return j * factorial(j - 1)
print(factorial(5))
