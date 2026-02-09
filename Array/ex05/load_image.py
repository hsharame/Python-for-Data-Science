from PIL import Image
import numpy as np
import os

def ft_load(path: str) -> np.ndarray:
    """
    Loads an image, prints its format, and its pixels
    content in RGB format.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File {path} does not exist")
    if not os.path.isfile(path):
        raise IsADirectoryError(f"{path} is directory")
    if not path.lower().endswith((".jpg", ".jpeg")):
        raise TypeError(f"{path}: unsupported format")
    try:
        im = Image.open(path)
    except IOError:
        raise AssertionError(f"Couldn't open {path}")

    im = im.convert("RGB")
    arr = np.array(im)
    print("The shape of image is:", arr.shape)
    return arr
