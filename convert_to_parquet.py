import os
import sys

import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor

import pandas as pd


def read_and_convert(table_dir, file, schemas):
    df = pd.read_csv(os.path.join(table_dir, file), sep="|", names=schemas[table], header=None)
    df.to_parquet(os.path.join(table_dir, "parquet", file.replace("tbl", "parquet")))


if __name__ == "__main__":
    base_dir = str(sys.argv[1])

    tables = [
        "customer",
        "lineitem",
        "nation",
        "orders",
        "part",
        "partsupp",
        "supplier",
        "region"
    ]

    schemas = {
        "region": ["r_regionkey", "r_name", "r_comment"],
        "nation": ["n_nationkey", "n_name", "n_regionkey", "n_comment"],
        "customer": ["c_custkey", "c_name", "c_address", "c_nationkey", "c_phone", "c_acctbal", "c_mktsegment", "c_comment"],
        "part": ["p_partkey", "p_name", "p_mfgr", "p_brand", "p_type", "p_size", "p_container", "p_retailprice", "p_comment"],
        "supplier": ["s_suppkey", "s_name", "s_address", "s_nationkey", "s_phone", "s_acctbal", "s_comment"],
        "partsupp": ["ps_partkey", "ps_suppkey", "ps_availqty", "ps_supplycost", "ps_comment"],
        "orders": ["o_orderkey", "o_custkey", "o_orderstatus", "o_totalprice", "o_orderdate", "o_orderpriority", "o_clerk", "o_shippriority", "o_comment"],
        "lineitem": ["l_orderkey", "l_partkey", "l_suppkey", "l_linenumber", "l_quantity", "l_extendedprice", "l_discount", "l_tax", "l_returnflag", "l_linestatus", "l_shipdate", "l_commitdate", "l_receiptdate", "l_shipinstruct", "l_shipmode", "l_comment"]
    }

    tables = ["lineitem"]

    for table in tables:
        table_dir = os.path.join(base_dir, table)
        os.makedirs(os.path.join(table_dir, "parquet"), exist_ok=True)
        print("Reading files from ", table_dir)

        with ThreadPoolExecutor(max_workers=mp.cpu_count()) as executor:
            for file in os.listdir(table_dir):
                executor.submit(read_and_convert, table_dir, file, schemas)
