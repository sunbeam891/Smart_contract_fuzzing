#Script_json_maker0.3
import json

codecov="-"
Branchcov="-"
vulndetected="-"
timetaken="-"
timetrigger="-"
Transactions = "-"
File_path= "coverage_json.json"

def coverage_json_maker():
    Dict={}
    Dict=dict({"Code_Coverage":codecov,"Branch_Coverage":Branchcov,"No._of_Transactions":Transactions, "Time_Taken": timetaken,"Time_trigger": timetrigger})
    with open(File_path, 'a', encoding="utf-8") as file:
        x = json.dumps(Dict, indent=4)
        file.write(x + '\n')