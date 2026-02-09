import numpy as np


def ft_invert(array) -> np.ndarray:
    """
Inverts the color of the image received.
    """
    inv = array.copy()
    inv[:, :, 0] = 255 - inv[:, :, 0]
    inv[:, :, 1] = 255 - inv[:, :, 1]
    inv[:, :, 2] = 255 - inv[:, :, 2]
    return inv


def ft_red(array) -> np.ndarray:
    """
Changes the color of the image to red.
    """
    red = array.copy()
    red[:, :, 1] = 0
    red[:, :, 2] = 0
    return red


def ft_green(array) -> np.ndarray:
    """
Changes the color of the image to green.
    """
    green = array.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0
    return green


def ft_blue(array) -> np.ndarray:
    """
Changes the color of the image to blue.
    """
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    return blue


def ft_grey(array) -> np.ndarray:
    """
Changes the color of the image to grey.
    """
    grey = array.copy()
    value = grey[:, :, 0] / 3 + grey[:, :, 1] / 3 + grey[:, :, 2] / 3
    grey[:, :, 0] = value
    grey[:, :, 1] = value
    grey[:, :, 2] = value
    return grey
