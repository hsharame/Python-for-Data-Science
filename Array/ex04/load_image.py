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
        im = Image.open(path).convert('L')
    except IOError:
        raise AssertionError(f"Couldn't open {path}")

    arr = np.array(im)
    h, w = arr.shape
    start_y = h // 2 - 200
    start_x = w // 2 - 100
    zoom = arr[start_y:start_y + 400, start_x:start_x + 400]
    zoom_expand = np.expand_dims(zoom, axis=2)
    print("The shape of image is:", zoom_expand.shape, "or", zoom.shape)
    print(zoom_expand)
    return arr
