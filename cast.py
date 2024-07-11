import sys

import pandas as pd

if __name__ == "__main__":
    filepath = str(sys.argv[1])
    print("Reading file ", filepath)

    if filepath.endswith("lineitem.parquet"):
        df = pd.read_parquet(filepath)
        df["l_linenumber"] = df["l_linenumber"].astype("int64")
        df["l_quantity"] = df["l_quantity"].astype("int64")
        df["l_shipdate"] = pd.to_datetime(df["l_shipdate"]).dt.strftime("%Y-%m-%d")
        df["l_commitdate"] = pd.to_datetime(df["l_commitdate"]).dt.strftime("%Y-%m-%d")
        df["l_receiptdate"] = pd.to_datetime(df["l_receiptdate"]).dt.strftime("%Y-%m-%d")
        df.to_parquet(filepath, index=False)
    
    elif filepath.endswith("part.parquet"):
        df = pd.read_parquet(filepath)
        df["p_size"] = df["p_size"].astype("int64")
        df.to_parquet(filepath, index=False)

    elif filepath.endswith("partsupp.parquet"):
        df = pd.read_parquet(filepath)
        df["ps_availqty"] = df["ps_availqty"].astype("int64")
        df.to_parquet(filepath, index=False)

    elif filepath.endswith("orders.parquet"):
        df = pd.read_parquet(filepath)
        df["o_shippriority"] = df["o_shippriority"].astype("int64")
        df["o_orderdate"] = pd.to_datetime(df["o_orderdate"])
        df.to_parquet(filepath, index=False)
    