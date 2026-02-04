from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def main():
    """
    Program loads the image "animal.jpeg", prints some information
    about it and displays it after "zooming".
    """
    try:
        print(ft_load("animal.jpeg"))
        im = Image.open("animal.jpeg").convert('L')
        # im.save('animal_gray.jpeg')
        arr = np.array(im)
        h, w = arr.shape
        start_y = h // 2 - 200
        start_x = w // 2 - 100
        zoom = arr[start_y:start_y + 400, start_x:start_x + 400]
        zoom_expand = np.expand_dims(zoom, axis=2)
        print("New shape after slicing:", zoom_expand.shape, "or", zoom.shape)
        print(zoom_expand)
        # plt.imshow(zoom)
        plt.imshow(zoom, cmap="gray")
        plt.show()
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()
