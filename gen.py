import os
import sys

import multiprocessing as mp

from concurrent.futures import ThreadPoolExecutor, as_completed


def generate(index, num_procs, table):
    os.system(f"dbgen -vf -s 100 -C {num_procs} -S {index} -T {table} -f")


if __name__ == "__main__":
    os.chdir("dbgen")
    table = str(sys.argv[1])
    db_gen_path = str(sys.argv[2])
    os.environ["DSS_PATH"] = db_gen_path
    num_procs = mp.cpu_count()
    with ThreadPoolExecutor(max_workers=num_procs) as executor:
        futures = list()
        for index in range(num_procs):
            futures.append(executor.submit(generate, index + 1, num_procs, table))

        for future in as_completed(futures):
            print(future.result())
