#Script_json_cov_per_time = v0.2
import json
import os
codecov="-"
Branchcov="-"
vulndetected=[]
timetaken="-"
Transactions = "-"
File_path= "cov_per_time.json"
Diction = {}
Diction["stats"]={}
branches = "-"
def cov_time_json_maker():
    if not os.path.exists(File_path):
        # Create file with JSON enclosures
        with open(File_path, 'w') as f:
            json.dump([], f)
    Dict={}
    Dict=dict({"Code_Coverage":codecov,"Branch_Coverage":Branchcov,"No._of_Transactions":Transactions, "Time_Taken": timetaken,"vulnerabilities":vulndetected,"branches":branches})
    with open(File_path, 'r+', encoding="utf-8") as file:
        file_data = json.load(file)
        file_data.append(Dict)
    with open(File_path, 'w') as f:
        json.dump(file_data, f, indent=3)