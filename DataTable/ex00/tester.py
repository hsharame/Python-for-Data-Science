from load_csv import load

try:
	print(load("landscape.jpg"))
except Exception as error:
    print(error)
