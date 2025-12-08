from typing import Iterable, Optional


def ft_filter(function: Optional, iterable: Iterable) -> object:
    """
    Return an iterator yielding those items of iterable for which function
    is true. If function is None, return the items that are true.
    """
    result = [x for x in iterable
              if (function is None and x)
              or (function is not None and function(x))]
    return iter(result)
