import sys


def main():
    """
    Program takes a string as an argument and encodes it into Morse Code.
    """
    NESTED_MORSE = {
        "A": ".- ",      "B": "-... ",    "C": "-.-. ",    "D": "-.. ",
        "E": ". ",       "F": "..-. ",    "G": "--. ",     "H": ".... ",
        "I": ".. ",      "J": ".--- ",    "K": "-.- ",     "L": ".-.. ",
        "M": "-- ",      "N": "-. ",      "O": "--- ",     "P": ".--. ",
        "Q": "--.- ",    "R": ".-. ",     "S": "... ",     "T": "- ",
        "U": "..- ",     "V": "...- ",    "W": ".-- ",     "X": "-..- ",
        "Y": "-.-- ",    "Z": "--.. ",
        "a": ".- ",      "b": "-... ",    "c": "-.-. ",    "d": "-.. ",
        "e": ". ",       "f": "..-. ",    "g": "--. ",     "h": ".... ",
        "i": ".. ",      "j": ".--- ",    "k": "-.- ",     "l": ".-.. ",
        "m": "-- ",      "n": "-. ",      "o": "--- ",     "p": ".--. ",
        "q": "--.- ",    "r": ".-. ",     "s": "... ",     "t": "- ",
        "u": "..- ",     "v": "...- ",    "w": ".-- ",     "x": "-..- ",
        "y": "-.-- ",    "z": "--.. ",
        "0": "----- ",   "1": ".---- ",   "2": "..--- ",   "3": "...-- ",
        "4": "....- ",   "5": "..... ",   "6": "-.... ",   "7": "--... ",
        "8": "---.. ",   "9": "----. ",   " ": "/ "}
    try:
        if len(sys.argv) == 2:
            s = sys.argv[1]
            for c in s:
                if not (c.isspace() or c.isdigit() or c.isalpha()):
                    raise AssertionError("the arguments are bad")
            print("".join(NESTED_MORSE[c] for c in s).rstrip())
        else:
            raise AssertionError("the arguments are bad")
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
