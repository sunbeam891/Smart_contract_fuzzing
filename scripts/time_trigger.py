#Script_json_time_trigger = v0.2 added vulnerabilities unique 
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
def trigger_json_maker():
    global vulnerabilities
    if not os.path.exists(File_path):
        # Create file with JSON enclosures
        with open(File_path, 'w') as f:
            json.dump([], f)
    if len(vulnerabilities)==0:
        vulnerabilities = ["_"]
    else:
        vulnerabilities = list(dict.fromkeys(vulnerabilities))
    Dict={}
    Dict=dict({"Code_Coverage":codecov,"Branch_Coverage":Branchcov,"No._of_Transactions":Transactions, "Time_Taken": timetaken,"vulnerabilities":vulnerabilities,"branches":branches})
    with open(File_path, 'r+', encoding="utf-8") as file:
        file_data = json.load(file)
        file_data.append(Dict)
    with open(File_path, 'w') as f:
        json.dump(file_data, f, indent=3)