from typing import Iterable, Optional


def ft_filter(function: Optional, iterable: Iterable) -> filter:
    """
    Return an iterator yielding those items of iterable for which function
    is true. If function is None, return the items that are true.
    """
    for element in iterable:
        if function is None:
            if element:
                yield element
        else:
            if function(element):
                yield element

# ages = [5, 12, 17, 18, 24, 32]
# def myFunc(x):
#   if x < 18:
#     return False
#   else:
#     return True
# print(list(ft_filter(myFunc, ages)))

# items = [0, 1, "", "Hello", None]
# print(list(ft_filter(None, items)))
