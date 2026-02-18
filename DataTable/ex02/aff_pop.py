from load_csv import load
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def parse_pop(value: str) -> float:
    s = value.lower()
    try:
        if s.endswith("m"):
            return float(s[:-1]) * 1000000
        if s.endswith("k"):
            return float(s[:-1]) * 1000
        else:
            return float(s)
    except ValueError:
        return None

def format_millions(value: float, pos: int) -> str:
    return f"{int(value / 1000000)}M"

def main():
    """
    Program loads population_total.csv file and
    displays the country information of your campus (France)
    versus Belarus
    """
    try:
        df = load("population_total.csv")
        line_france = df[df["country"] == "France"].iloc[0] #series
        line_belarus = df[df["country"] == "Belarus"].iloc[0]

        y_fr = line_france.drop("country").apply(parse_pop)
        y_by = line_belarus.drop("country").apply(parse_pop)
        years = y_fr.index.astype(int)
        mask = years <= 2050
        x = years[mask]
        y_fr = y_fr[mask]
        y_by = y_by[mask]

        # plot() is used to draw points (markers) in a diagram
        plt.plot(x, y_fr, label="France")
        plt.plot(x, y_by, label="Belarus")

        ticks_x = np.arange(x.min(), x.max() + 1, 40)
        plt.xticks(ticks_x)
        ticks_y = np.arange(0, y_fr.max() + 1, 20000000)
        plt.yticks(ticks_y)

        ax = plt.gca()
        ax.yaxis.set_major_formatter(FuncFormatter(format_millions))

        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.title("Population Projections")
        plt.legend(loc="lower right")
        plt.show()
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()
