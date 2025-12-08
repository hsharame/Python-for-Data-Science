from ft_filter import ft_filter

print(filter.__doc__)

ages = [5, 12, 17, 18, 24, 32]
def myFunc(x):
  if x < 18:
    return False
  else:
    return True
print(list(ft_filter(myFunc, ages)))
print(list(filter(myFunc, ages)))
print(ft_filter(myFunc, ages))
print(filter(myFunc, ages))

items = [0, 1, "", "Hello", None]
print(list(ft_filter(None, items)))
print(list(filter(None, items)))
