from load_csv import load

try:
    res = load("life_expectancy_years.csv")
    print(res)
except Exception as error:
    print(error)
