#Script_json_cov_per_time = v0.3 costumized to not add to file at each append
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
Main_file_data = []
def cov_time_json_maker():
    global Main_file_data
    Dict={}
    Dict=dict({"Code_Coverage":codecov,"Branch_Coverage":Branchcov,"No._of_Transactions":Transactions, "Time_Taken": timetaken,"vulnerabilities":vulndetected,"branches":branches})
    Main_file_data.append(Dict)

def file_creator():
    global Main_file_data
    with open(File_path, 'w') as f:
        json.dump(Main_file_data, f, indent=3)