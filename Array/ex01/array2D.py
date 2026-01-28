import numpy as np

def slice_me(family: list, start: int, end: int) -> list: 
    """
    Takes as parameters a 2D array, prints its shape, and returns a
    truncated version of the array based on the provided start and end arguments.
    """
    if (
        not isinstance(family, list)
        or not isinstance(start, int)
        or not isinstance(end, int)
    ):
        raise TypeError("Args must be: list, int, int")
    if not all(isinstance(row, list) for row in family):
        raise TypeError("A 2D list expected")
    row_len = len(family[0])
    if not all(len(row) == row_len for row in family):
        raise TypeError("Lists are not the same size")
    arr = np.array(family)
    print("My shape is :", arr.shape)
    res = arr[start:end]
    print("My new shape is :", res.shape)
    return res.tolist()