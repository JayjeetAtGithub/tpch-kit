import pandas as pd


if __name__ == "__main__":
    parquet_file_list = str(sys.argv[1])
    base_df = pd.read_parquet(parquet_file_list[0])
    for file in parquet_file_list[1:]:
        df = pd.read_parquet(file)
        base_df = base_df.append(df)
    base_df.to_parquet("agg.parquet")
