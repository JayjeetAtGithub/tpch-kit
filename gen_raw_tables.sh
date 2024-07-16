#!/bin/bash
set -e

scale_factor=$1
dataset_dir="/raid/tpch_sf$scale_factor"

mkdir -p ${dataset_dir}/lineitem
mkdir -p ${dataset_dir}/customer
mkdir -p ${dataset_dir}/orders
mkdir -p ${dataset_dir}/part
mkdir -p ${dataset_dir}/partsupp
mkdir -p ${dataset_dir}/supplier
mkdir -p ${dataset_dir}/nation
mkdir -p ${dataset_dir}/region

python3 gen.py L ${dataset_dir}/lineitem 96 ${scale_factor}
python3 gen.py O ${dataset_dir}/orders 96 ${scale_factor}
python3 gen.py S ${dataset_dir}/partsupp 64 ${scale_factor}
python3 gen.py P ${dataset_dir}/part 32 ${scale_factor}
python3 gen.py c ${dataset_dir}/customer 32 ${scale_factor}
python3 gen.py s ${dataset_dir}/supplier 10 ${scale_factor}
python3 gen.py n ${dataset_dir}/nation 1 ${scale_factor}
python3 gen.py r ${dataset_dir}/region 1 ${scale_factor}
