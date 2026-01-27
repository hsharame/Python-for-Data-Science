import numpy as np

def slice_me(family: list, start: int, end: int) -> list: 
    """
    Takes as parameters a 2D array, prints its shape, and returns a
    truncated version of the array based on the provided start and end arguments.
    """
    arr = np.array(family)
    print("My shape is :", arr.shape)
    res = arr[start:end]
    print("My new shape is :", res.shape)
    return res.tolist()

