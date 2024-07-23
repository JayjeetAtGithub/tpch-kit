import os
import sys

import pandas as pd

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_snappy.py <dataset_dir>")
        sys.exit(1)

    dataset_dir = str(sys.argv[1])

    tables = ["lineitem", "orders", "part", "supplier", "customer", "nation", "region", "partsupp"]
    for table in tables:
        filename = os.path.join(dataset_dir, table + ".parquet")
        df = pd.read_parquet(filename)
        df.to_parquet(filename, compression="snappy")
