def factorial(k):
  if k == 0:
    return 1
  else:
    return k * factorial(k - 1)
print(factorial(5))
