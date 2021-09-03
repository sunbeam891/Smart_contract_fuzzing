#Script_sfuzz_file_v0.1
#Format = python3 Sfuzz_creator.py <con_file> <con_name> <contract_folder> <dataset location> 
import os
import sys
import pandas as pd
#files = os.listdir(path)
#word = "contract"
#fuzzer = sys.argv[1]
#datasetloc = sys.argv[2]
#rootdirectory = sys.argv[3]



con_file = sys.argv[1]
con_name  =sys.argv[2]
Contract_folder = sys.argv[3]
datasetloc = sys.argv[4]


for root, dirs, files in os.walk(datasetloc):
    for file in files:
        if file == con_file:
            a_file= open(os.path.join(root, file),"r",encoding="utf-8")
            #print(os.path.join(root, file))
            listoflines=a_file.readlines()
            new_file = con_name + ".sol"
            b_file=open(os.path.join(Contract_folder, new_file),"w+",encoding="utf-8")
            b_file.writelines(listoflines)
            b_file.close()