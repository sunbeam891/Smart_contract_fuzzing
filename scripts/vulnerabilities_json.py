#Script_json_maker_vulnerabilities_adder0.4
import json

codecov="-"
Branchcov="-"
Vulnerability_detected="No" #Read from file
Vulnerabilities_detected = []
#Vulnerabilities_detected = ",".join(Vulnerabilities_detected)
File_path= "vuln_json.json"

def vuln_Jsonmaker():
    Dict={}
    if len(Vulnerabilities_detected)==0:
        Dict=dict({"Vulnerabilities_detected":"_"})
    else:
        Dict=dict({"Vulnerabilities_detected":list(dict.fromkeys(Vulnerabilities_detected))})
    with open(File_path, 'w', encoding="utf-8") as file:
        x = json.dumps(Dict, indent=4)
        file.write(x + '\n')