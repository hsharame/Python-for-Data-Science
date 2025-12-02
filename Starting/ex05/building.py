import sys

def main():
    """
    Description
    """
	try:
		if len(sys.argv) == 2:
			input = sys.argv[1]
		elif len(sys.argv) < 2 or len(sys.argv[1]) == 0:
			input = input("What is the text to count?")
		else:
			raise AssertionError("more than one argument is provided")
	except AssertionError as error:
		print(f"AssertionError: {error}")
	print(f"The text contains {sum(1 for c in input)} characters:")

if __name__ == "__main__":
	main()
