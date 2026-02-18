from load_csv import load
import numpy as np
import matplotlib.pyplot as plt

def main():
    """
    Program loads life_expectancy_years.csv file and
    displays the country information of your campus (France)
    """
    try:
        df = load("life_expectancy_years.csv")
        line = df[df["country"] == "France"].iloc[0]
        print(line)

        y = line.drop("country")
        x = y.index.astype(int)
        plt.plot(x, y)
        ticks = np.arange(x.min(), x.max() + 1, 40)
        plt.xticks(ticks)
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.title("France Life expectancy Projections")
        plt.show()
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()
