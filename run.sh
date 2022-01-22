#!/bin/bash
set -e

cd dbgen/
make MACHINE=LINUX

rm -rf /mnt/cephfs/tpch_sf100/*
mkdir -p /mnt/cephfs/tpch_sf100/lineitem
mkdir -p /mnt/cephfs/tpch_sf100/customer
mkdir -p /mnt/cephfs/tpch_sf100/orders
mkdir -p /mnt/cephfs/tpch_sf100/part
mkdir -p /mnt/cephfs/tpch_sf100/partsupp
mkdir -p /mnt/cephfs/tpch_sf100/supplier
mkdir -p /mnt/cephfs/tpch_sf100/nation
mkdir -p /mnt/cephfs/tpch_sf100/region

echo "Now execute : "
echo "python3 gen.py <table> <path>"

# supplier: 140MB

