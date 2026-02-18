import numpy as np
import pandas as pd
import os


def load(path: str) -> pd.DataFrame :
    """
    Function takes a path as argument, writes the dimensions
    of the data set and returns it.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File {path} does not exist")
    if not os.path.isfile(path):
        raise IsADirectoryError(f"{path} is directory")
    if not path.lower().endswith((".csv")):
        raise TypeError(f"{path}: unsupported format")
    try:
        df = pd.read_csv(path)
    except Exception as error:
        raise Exception(f"Couldn't read {path}")
    print("Loading dataset of dimensions", df.shape)

    return df
