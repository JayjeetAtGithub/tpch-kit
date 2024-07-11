import os
import sys

import pandas as pd

if __name__ == "__main__":
    dataset_path = str(sys.argv[1])
    tables = ["lineitem", "orders", "part", "partsupp"]
    for table in tables:
        filepath = os.path.join(dataset_path, f"{table}.parquet")
        print("Reading file ", filepath)

        if filepath.endswith("lineitem.parquet"):
            df = pd.read_parquet(filepath)
            df["l_linenumber"] = df["l_linenumber"].astype("int64")
            df["l_quantity"] = df["l_quantity"].astype("int64")
            df["l_shipdate"] = df["l_shipdate"].astype("int32")
            df["l_commitdate"] = df["l_commitdate"].astype("int32")
            df["l_receiptdate"] = df["l_receiptdate"].astype("int32")
            df.to_parquet(filepath, index=False, engine="pyarrow")
        
        elif filepath.endswith("part.parquet"):
            df = pd.read_parquet(filepath)
            df["p_size"] = df["p_size"].astype("int64")
            df.to_parquet(filepath, index=False, engine="pyarrow")

        elif filepath.endswith("partsupp.parquet"):
            df = pd.read_parquet(filepath)
            df["ps_availqty"] = df["ps_availqty"].astype("int64")
            df.to_parquet(filepath, index=False, engine="pyarrow")

        elif filepath.endswith("orders.parquet"):
            df = pd.read_parquet(filepath)
            df["o_shippriority"] = df["o_shippriority"].astype("int64")
            df["o_orderdate"] = df["o_orderdate"].astype("str")
            df.to_parquet(filepath, index=False, engine="pyarrow")
        