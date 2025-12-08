import sys
import string
from ft_filter import ft_filter


def main():
    """
    Program accepts two arguments: a string (S) and an integer (N).
    The program output a list of words from S that have a length greater than N
    """
    try:
        if len(sys.argv) == 3:
            s = sys.argv[1]
            try:
                n = int(sys.argv[2])
            except ValueError:
                raise AssertionError("the arguments are bad")
            for c in s:
                if c in string.punctuation or c.isspace() and c != " ":
                    raise AssertionError("the arguments are bad")
            words = s.split()
            filtered = ft_filter(lambda w: len(w) > n, words)
            result = [w for w in filtered]
            print(result)
        else:
            raise AssertionError("the arguments are bad")
    except AssertionError as error:
        print(f"AssertionError: {error}")


def greater_than_n(s: str, number: int):
    """
    Return True if length of S is greater than NUMBER.
     Otherwise, return False.
    """
    if len(s) > number:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
