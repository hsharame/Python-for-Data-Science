from PIL import Image
import numpy as np

def ft_load(path: str) -> list:
    """
    Loads an image, prints its format, and its pixels
    content in RGB format.
    """
    im = Image.open(path)
    im = im.convert("RGB")
    arr = np.array(im)
    print("The shape of image is:", arr.shape)
    return list(im.getdata())