import sys

import pandas as pd

if __name__ == "__main__":
    filepath = str(sys.argv[1])
    df = pd.read_parquet(filepath)

    df["l_quantity"] = df["l_quantity"].astype("int64")

    df.to_parquet(filepath, index=False)