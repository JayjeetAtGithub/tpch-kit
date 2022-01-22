#!/bin/bash
set -e

cd dbgen/
make MACHINE=LINUX

rm -rf /mnt/cephfs/dataset/*
mkdir -p /mnt/cephfs/dataset/lineitem
mkdir -p /mnt/cephfs/dataset/customer
mkdir -p /mnt/cephfs/dataset/orders
mkdir -p /mnt/cephfs/dataset/part
mkdir -p /mnt/cephfs/dataset/partsupp
mkdir -p /mnt/cephfs/dataset/supplier
mkdir -p /mnt/cephfs/dataset/nation
mkdir -p /mnt/cephfs/dataset/region

echo "Now execute : "
echo "python3 gen.py <table> <path> <procs>"
