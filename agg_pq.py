import os
import sys

import pandas as pd


if __name__ == "__main__":
    base_dir = str(sys.argv[1])

    # tables = [
    #     "customer",
    #     "lineitem",
    #     "nation",
    #     "orders",
    #     "part",
    #     "partsupp",
    #     "supplier",
    #     "region"
    # ]

    tables = ["customer"]

    for table in tables:
        table_parquet_dir = os.path.join(base_dir, table, "parquet")
        table_parquet_files = os.listdir(table_parquet_dir)
        print("Merging ", len(table_parquet_files), " files from ", table_parquet_dir)
        df_list = list()
        for idx, file in enumerate(table_parquet_files):
            print("Reading file ", idx, " : ", os.path.join(table_parquet_dir, file))
            df = pd.read_parquet(os.path.join(table_parquet_dir, file))
            df_list.append(df)
        final_df = pd.concat(df_list)
        final_df.to_parquet(os.path.join(base_dir, table + ".parquet"))
