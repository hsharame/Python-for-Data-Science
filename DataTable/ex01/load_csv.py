import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """
    Function takes a path as argument, writes the dimensions
    of the data set and returns it.
    """
    if not os.path.exists(path):
        print(f"File {path} does not exist")
        return None
    if not os.path.isfile(path):
        print(f"{path} is directory")
        return None
    if not path.lower().endswith((".csv")):
        print(f"{path}: unsupported format")
        return None
    try:
        df = pd.read_csv(path)
    except Exception:
        print(f"Couldn't read {path}")
        return None
    print("Loading dataset of dimensions", df.shape)

    return df
