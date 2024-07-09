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
        base_df = pd.read_parquet(os.path.join(table_parquet_dir, table_parquet_files[0]))
        for file in table_parquet_files[1:]:
            df = pd.read_parquet(os.path.join(table_parquet_dir, file))
            base_df = base_df.append(df)
        base_df.to_parquet(os.path.join(base_dir, table + ".parquet"))
