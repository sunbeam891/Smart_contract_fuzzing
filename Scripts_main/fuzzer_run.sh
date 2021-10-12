#!/bin/bash
FUZZER=$1
DATASET=$2
ROOT=$3
ID=$4
SAVETO=$5

python3 Command_cr.py ${FUZZER} ${DATASET} ${ROOT} ${ID} ${SAVETO}

chmod +x ${DATASET}/${FUZZER}_commands${ID}.sh

./${DATASET}/${FUZZER}_commands${ID}.sh    