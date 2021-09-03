#script0.3.3

# Format : python3 Test.py <Contractname> <ContractFilename>

import os
import sys
#files = os.listdir(path)
word = "contract"
delim = " "
words= []
path =""
commands = open ("Confuzzius_commands.sh","w")
commands.write ("#!/bin/bash" + " \n")
commands.write("cd /root/" + " \n")
contractname = sys.argv[1]
Contractfile = sys.argv[2]


#add if else for different fuzzers for a variable that contains the directory containing the crowdsale folder


#Remove build files
for root, dirs, files in os.walk("/go/src/ilf/example/crowdsale"):
    print(files)
    for directory in dirs:
        if directory == "build":
            print(os.path.join(root, directory))
            os.system ("rm -r  "+ os.path.join(root, directory))



# Edit deploy js file with contract details
for root, dirs, files in os.walk("/go/src/ilf/example/crowdsale"):
    for f in files:
        if f == "2_deploy_contracts.js":
            a_file= open(os.path.join(root, f),"r",encoding="utf-8")
            listoflines=a_file.readlines()
            print(listoflines)
            for i in range(0,len(listoflines)):
                
                #if line.find("deployer.deploy") != -1:
                if "var crowdsale " in listoflines[i]:
                    listoflines[i]='var crowdsale = artifacts.require("{contractsname}");\n'.format(contractsname=contractname)
                    print(listoflines)
            print(listoflines)
            b_file=open(os.path.join(root, f),"w",encoding="utf-8")
            b_file.writelines(listoflines)
            b_file.close()
            a_file.close()
                    

# Copy new contract and delete old contract
for root2, dirs2, files2 in os.walk("/go/src/ilf/example/crowdsale/contracts"):
    for f in files2:
        if f == "Migrations.sol":
            path = root2
        else:
            os.system ("rm " + os.path.join(root2, f))
for root3, dirs3, files3 in os.walk("/go/src/ilf/dataset"):
    for f in files3:
        if f == Contractfile:
            os.system ("cp " + os.path.join(root3, f) + " " + path)