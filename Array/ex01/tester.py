from array2D import slice_me

family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

print("*" * 50)
try: 
    family = [[1.80, 78.4], 6]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))
except Exception as error:
    print(error)

print("*" * 50)
try: 
    family = [[1.80, 78.4], [2.15, 12.7], [2.15, 102.7, 67,9]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))
except Exception as error:
    print(error)

print("*" * 50)
try: 
    family = ("Hello", "toto!")
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))
except Exception as error:
    print(error)

print("*" * 50)
try: 
    family = [["Hello", "tata!"],
    {"Hello" : "titi!"}]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))
except Exception as error:
    print(error)