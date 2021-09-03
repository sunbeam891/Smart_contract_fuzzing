#Script_sFuzz_data_retriever_v0.6
#format = python3 sfuzz_data_retr.py <filename> <contractname> <contracts_folder>
import json
import os
from decimal import Decimal
import sys
from openpyxl import load_workbook
import pandas as pd
import coverage_json
import vulnerabilities_json

filename = sys.argv[1]
Contractname = sys.argv[2] 
contracts_fold = sys.argv[3] 
for root, dirs, files in os.walk(contracts_fold):
            for file in files:
                if file == "stats.json":
                    File = os.path.join(root, file)

if os.path.isfile(File) == False or os.stat(File).st_size == 0 :
    sys.exit()


with open(File, 'r',encoding="utf-8") as f:
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
            vulnerabilities_json.Vulnerabilities_detected.append("gasless")
        elif key == "dangerous delegatecall":
            vulnerabilities_json.Vulnerabilities_detected.append("DangerousDelegatecall")
        elif key == "exception disorder":
            vulnerabilities_json.Vulnerabilities_detected.append("UnhandledException")
        elif key == "freezing ether":
            vulnerabilities_json.Vulnerabilities_detected.append("Locking")
        elif key == "reentrancy":
            vulnerabilities_json.Vulnerabilities_detected.append("Reentrancy")
        elif key == "integer overflow":
            vulnerabilities_json.Vulnerabilities_detected.append("Overflow")
        elif key == "timestamp dependency":
            vulnerabilities_json.Vulnerabilities_detected.append("BlockStateDep")
        elif key == "integer underflow":
            vulnerabilities_json.Vulnerabilities_detected.append("Overflow") 
        elif key == "block number dependency":
            vulnerabilities_json.Vulnerabilities_detected.append("BlockStateDep")     

coverage_json.Branchcov = Branch_coverage
coverage_json.Transactions = total_execs
coverage_json.timetaken = time_taken
coverage_json.coverage_json_maker()
vulnerabilities_json.vuln_Jsonmaker()