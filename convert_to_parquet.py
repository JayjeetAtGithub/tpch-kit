import os
import sys

import pandas as pd


if __name__ == "__main__":
    base_dir = str(sys.argv[1])

    tables = [
        "region"
    ]

    for table in tables:
        table_dir = os.path.join(base_dir, table)
        print("Reading files from", table_dir)
        for file in os.listdir(table_dir):
            if file.endswith(".tbl"):
                df = pd.read_csv(os.path.join(table_dir, file), sep="|", header=None)
                print(df)
                df.to_parquet(os.path.join(table_dir, file.replace(".csv", ".parquet")))
