#Script_sFuzz_data_retriever_v0.14
#format = python3 sfuzz_per_time_retr.py <filename> <contractname> <contracts_folder>
import json
import os
from decimal import Decimal
import sys
from openpyxl import load_workbook
import pandas as pd
import cov_per_time
import time_trigger
from natsort import natsorted, ns

filename = sys.argv[1]
Contractname = sys.argv[2] 
file_list = []
file_location = []
contracts_fold = sys.argv[3] 
for root, dirs, files in os.walk(contracts_fold):
            for file in files:
                if "stats" in file and not file in file_list:
                    File = os.path.join(root, file)
                    file_list.append(file)
                    file_location.append(File)


Sorted_list =[]
Sorted_list = natsorted(file_location,alg=ns.IGNORECASE)


for final_file in Sorted_list:
    if os.path.isfile(final_file) == False or os.stat(File).st_size == 0 :
        sys.exit()
    
    with open(final_file, 'r',encoding="utf-8") as f:
        vuln_json = json.load(f)
    
    dur = float(vuln_json["duration"])
    #time = "{:.2f}".format(*100)
    time_taken = "{:.2f} secs".format(dur)
    total_execs = vuln_json["totalExecs"]
    vulnerabilities =  vuln_json["vulnerabilities"]
    branches = vuln_json["branches"]
    Branch_coverage = "{} % ({})".format(vuln_json["coverage"],vuln_json["branches"])
    for key,value in vulnerabilities.items():
        if value != "0":
            if key == "gasless send":
                cov_per_time.vulndetected.append("gasless")
                time_trigger.vulnerabilities.append("gasless")
            elif key == "dangerous delegatecall":
                cov_per_time.vulndetected.append("DangerousDelegatecall")
                time_trigger.vulnerabilities.append("DangerousDelegatecall")
            elif key == "exception disorder":
                cov_per_time.vulndetected.append("UnhandledException")
                time_trigger.vulnerabilities.append("UnhandledException")
            elif key == "freezing ether":
                cov_per_time.vulndetected.append("Locking")
                time_trigger.vulnerabilities.append("Locking")
            elif key == "reentrancy":
                cov_per_time.vulndetected.append("Reentrancy")
                time_trigger.vulnerabilities.append("Reentrancy")
            elif key == "integer overflow":
                cov_per_time.vulndetected.append("Overflow")
                time_trigger.vulnerabilities.append("Overflow")
            elif key == "timestamp dependency":
                cov_per_time.vulndetected.append("BlockStateDep")
                time_trigger.vulnerabilities.append("BlockStateDep")
            elif key == "integer underflow":
                cov_per_time.vulndetected.append("Overflow") 
                time_trigger.vulnerabilities.append("Overflow")
            elif key == "block number dependency":
                cov_per_time.vulndetected.append("BlockStateDep")
                time_trigger.vulnerabilities.append("BlockStateDep")
    cov_per_time.Branchcov = Branch_coverage
    time_trigger.Branchcov = Branch_coverage
    cov_per_time.Transactions = total_execs
    cov_per_time.timetaken = time_taken
    time_trigger.timetaken = time_taken
    cov_per_time.branches= branches
    cov_per_time.cov_time_json_maker()
    time_trigger.trigger_json_maker()
cov_per_time.file_creator()
time_trigger.file_creator()    