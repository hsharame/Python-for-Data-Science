from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import mplcursors as mpl


def format_k(value: float, pos: int) -> str:
    return f"{int(value / 1000)}k"


def main():
    """
    Program loads the files
    "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    and "life_expectancy_years.csv", and displays the projection of
    life expectancy in relation to the gross national product of
    the year 1900 for each country.
    """
    try:
        df_gdp = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
            )
        df_le = load("life_expectancy_years.csv")
        line_gdp = df_gdp[["country", "1900"]]
        line_le = df_le[["country", "1900"]]
        df_1900 = line_gdp.merge(
            line_le, on="country", suffixes=("_gdp", "_le")
            )

        y = df_1900["1900_le"]
        x = df_1900["1900_gdp"]
        sc = plt.scatter(x, y)

        # Series with index access
        countries = df_1900["country"]
        # Creates a cursor object that monitors and triggers
        # the display on hover for scatter plot
        cursor = mpl.cursor(sc, hover=True)

        # Decorator. sel - selection object

        @cursor.connect("add")
        def on_add(sel):
            i = sel.index
            sel.annotation.set_text(f"{countries[i]}")

        # logarithmic scale on the X-axis
        plt.xscale("log")

        ax = plt.gca()
        ax.xaxis.set_major_formatter(FuncFormatter(format_k))

        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.title("1900")
        plt.show()

    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
