from load_image import ft_load

print(ft_load("landscape.jpg"))

try:
    print(ft_load("t.png"))
except Exception as error:
    print(error)