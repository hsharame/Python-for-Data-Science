import sys

if len(sys.argv) > 1:
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        try:
            n = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")
        print("I'm Even." if n % 2 == 0 else "I'm Odd.")
    except AssertionError as error:
        print(f"AssertionError: {error}")
