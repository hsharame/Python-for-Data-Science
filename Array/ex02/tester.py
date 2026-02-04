from load_image import ft_load

print(ft_load("landscape.jpg"))
print("*" * 50)
try:
    print(ft_load("t.png"))
except Exception as error:
    print(error)
