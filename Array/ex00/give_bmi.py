def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Takes 2 lists of integers or floats as input and returns a list
    of BMI values.
    """
    res = [w / h ** 2 for w, h in zip(weight, height)]
    return res


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Accepts a list of integers or floats and an integer representing
    a limit as parameters. It returns a list of booleans (True if above the limit).
    """
    res = [x >= limit for x in bmi]
    return res