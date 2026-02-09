def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    Takes 2 lists of integers or floats as input and returns a list
    of BMI values.
    """
    if len(height) != len(weight):
        raise ValueError("Lists must be of the same length")
    for w, h in zip(weight, height):
        if not isinstance(w, (int, float)) or not isinstance(h, (int, float)):
            raise TypeError("Lists must contain only integers or floats")
        if w <= 0 or h <= 0:
            raise ValueError("Height and weight must be greater than 0")
    res = [w / h ** 2 for w, h in zip(weight, height)]
    return res


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Accepts a list of integers or floats and an integer representing
    a limit as parameters. It returns a list of booleans
    (True if above the limit).
    """
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer")
    for x in bmi:
        if not isinstance(x, (int, float)):
            raise TypeError("List must contain only integers or floats")
    res = [x >= limit for x in bmi]
    return res
