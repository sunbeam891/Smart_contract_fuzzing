#script0.3

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
print ("entered truffle maker")
#Remove build files
for root, dirs, files in os.walk("/root/dataset/crowdsale"):
    for directory in dirs:
        if directory == "build":
            #print(os.path.join(root, directory))
            os.system ("rm -r "+ os.path.join(root, directory))



# Edit deploy js file with contract details
for root, dirs, files in os.walk("/root/dataset/crowdsale"):
    print(files)
    for f in files:
        if f == "2_deploy_contracts.js":
            a_file= open(os.path.join(root, f),"r",encoding="utf-8")
            listoflines=a_file.readlines()
            print(listoflines)
            for i in range(0,len(listoflines)):
                
                #if line.find("deployer.deploy") != -1:
                if "var crowdsale " in listoflines[i]:
                    listoflines[i]='var crowdsale = artifacts.require("{contractname}");'.format(contractname=contractname)
        b_file=open(os.path.join(root, f),"w",encoding="utf-8")
        b_file.writelines(listoflines)
        b_file.close()
                    

# Copy new contract and delete old contract
for root, dirs, files in os.walk("/root/dataset/crowdsale/contracts"):
    for f in files:
        if f == "Migrations.sol":
            path = root
        else:
            os.system ("rm " + os.path.join(root, f))
for root, dirs, files in os.walk("/root/dataset"):
    for f in files:
        if f == Contractfile:
            os.system ("cp " + os.path.join(root, f) + " " + path)