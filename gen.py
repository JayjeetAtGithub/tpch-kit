import os
import sys

from concurrent.futures import ThreadPoolExecutor, as_completed


def generate(index, num_procs, table):
    os.system(f"dbgen -vf -s 100 -C {num_procs} -S {index} -T {table} -f")


if __name__ == "__main__":
    os.chdir("dbgen")
    table_shortcut = str(sys.argv[1])
    dataset_path = str(sys.argv[2])
    num_procs = int(sys.argv[3])

    os.environ["DSS_PATH"] = dataset_path
    with ThreadPoolExecutor(max_workers=num_procs) as executor:
        futures = list()
        for index in range(num_procs):
            futures.append(executor.submit(generate, index + 1, num_procs, table_shortcut))

        for future in as_completed(futures):
            print(future.result())
