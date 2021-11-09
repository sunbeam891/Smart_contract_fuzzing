#!/bin/bash
FUZZER=$1
DATASET=$2
ROOT=$3
ID=$4
SAVETO=$5
cd ${DATASET}
python3 ${DATASET}/Command_cr.py ${FUZZER} ${DATASET} ${ROOT} ${ID} ${SAVETO}

chmod +x ${FUZZER}_commands${ID}.sh

./${FUZZER}_commands${ID}.sh    
