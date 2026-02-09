from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey
import matplotlib.pyplot as plt

try:
    array = ft_load("landscape.jpg")
    inv = ft_invert(array)
    red = ft_red(array)
    green = ft_green(array)
    blue = ft_blue(array)
    grey = ft_grey(array)
    plt.imshow(array)
    plt.show()
    plt.imshow(inv)
    plt.show()
    plt.imshow(red)
    plt.show()
    plt.imshow(green)
    plt.show()
    plt.imshow(blue)
    plt.show()
    plt.imshow(grey)
    plt.show()
    print(ft_invert.__doc__)
except Exception as error:
    print(error)
