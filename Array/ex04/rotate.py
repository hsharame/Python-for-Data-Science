from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def main():
    """
    Program loads the image "animal.jpeg", cuts a square part from it,
    manually transposes the image, displays it, and prints its new shape
    and pixel data after the transpose.
    """
    try:
        ft_load("animal.jpeg")
        im = Image.open("animal.jpeg").convert('L')
        arr = np.array(im)
        h, w = arr.shape
        start_y = h // 2 - 200
        start_x = w // 2 - 100
        zoom = arr[start_y:start_y + 400, start_x:start_x + 400]
        print("New shape after Transpose:", zoom.shape)
        new_image = np.zeros((400, 400), dtype=zoom.dtype)
        for i in range(400):
            for j in range(400):
                new_image[j][i] = zoom[i][j]
        print(new_image)
        plt.imshow(new_image, cmap="gray")
        plt.show()
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()
