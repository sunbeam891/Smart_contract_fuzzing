#Script_json_time_trigger = v0.3 costumized to not add to file at each append 
import json
import os
codecov="-"
Branchcov="-"
vulndetected="_"
vulnerabilities = []
timetaken="-"
Transactions = "-"
File_path= "trigger_time.json"
Diction = {}
Diction["stats"]={}
branches = "-"
Main_file_data = []
def trigger_json_maker():
    global vulnerabilities
    global Main_file_data
    if len(vulnerabilities)==0:
        vulnerabilities = ["_"]
    else:
        vulnerabilities = list(dict.fromkeys(vulnerabilities))
    Dict={}
    Dict=dict({"Code_Coverage":codecov,"Branch_Coverage":Branchcov,"No._of_Transactions":Transactions, "Time_Taken": timetaken,"vulnerabilities":vulnerabilities,"branches":branches})
    Main_file_data.append(Dict)

def file_creator():
    global Main_file_data
    with open(File_path, 'w') as f:
        json.dump(Main_file_data, f, indent=3)