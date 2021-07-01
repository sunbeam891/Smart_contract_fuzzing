#script0.4

# Format: python3 test.py <Fuzzer> <datasetlocation> <rootdirectoryforrunningfuzzer (/root/)>
import os
import sys
#files = os.listdir(path)
word = "contract"
delim = " "
words= []
fuzzer = sys.argv[1]
datasetloc = sys.argv[2]
rootdirectory = sys.argv[3]
commands = open ("Confuzzius_commands.sh","w")
commands.write ("#!/bin/bash" + " \n")
commands.write("cd "+  rootdirectory + " \n")
contractname=""
count = 0

if fuzzer == "Confuzzius":

    for root, dirs, files in os.walk(datasetloc):
        for file in files:
            if file.endswith(".sol"):
                count=count+1
                print(count)

                a_file= open(os.path.join(root, file),"r",encoding="utf-8")
                #print(os.path.join(root, file))
                listoflines=a_file.readlines()
                for i in range (0,len(listoflines)):
                    s_line = listoflines[i].strip().split(" ")
                    if s_line[0] == "pragma":
                        listoflines[i] = "pragma solidity 0.4.26;\n"
                b_file=open(os.path.join(root, file),"w",encoding="utf-8")
                b_file.writelines(listoflines)
                b_file.close()

                with open(os.path.join(root, file),encoding="utf-8") as f:
                    for line in f:
                        #print(line)
                        s_line = line.strip().split(delim)
                        #print(s_line[s_line.index(word) + 1])
                        #print(s_line)
                        if s_line[0]== word:
                            contractname=s_line[1]
                            contractname=contractname.replace("{","")
                            Confuzzius_bash_run= "python3 fuzzer/main.py -s " + os.path.join(root, file) +" -c "+ contractname+ " --solc v0.4.26 --evm byzantium -t 10"
                            #print (Confuzzius_bash_run)
                            commands.write ("echo '"+"File name = "+file  + " Contract Name = " +contractname+ "'\n")
                            commands.write ("echo '"+Confuzzius_bash_run + "'\n")
                            commands.write (Confuzzius_bash_run + "\n")
                            commands.write ('read -p "Are you sure? " -n 1 -r choice' + ' \n\n\n\n\n')
                            
                            
elif fuzzer == "ILF":
    for root, dirs, files in os.walk(datasetloc):
        for file in files:
            if file.endswith(".sol"):

                a_file= open(os.path.join(root, file),"r",encoding="utf-8")
                #print(os.path.join(root, file))
                listoflines=a_file.readlines()
                for i in range (0,len(listoflines)):
                    s_line = listoflines[i].strip().split(" ")
                    if s_line[0] == "pragma":
                        listoflines[i] = "pragma solidity 0.4.25;\n"
                b_file=open(os.path.join(root, file),"w",encoding="utf-8")
                b_file.writelines(listoflines)
                b_file.close()

                with open(os.path.join(root, file),encoding="utf-8") as f:
                    for line in f:
                        #print(line)
                        s_line = line.strip().split(delim)
                        #print(s_line[s_line.index(word) + 1])
                        #print(s_line)
                        if s_line[0]== word:
                            contractname=s_line[1]
                            contractname=contractname.replace("{","")
                            ILF_bash_run= "python3 -m ilf --proj ." + rootdirectory+ "/crowdsale" +" --contract "+ contractname+ " --fuzzer imitation --model ./model/ --limit 2000"
                            Truffle_maker= "python3 Test.py "+ contractname + " "+ file
                            commands.write ("echo '"+"File name = "+file  + " Contract Name = " +contractname+ "'\n'")
                            commands.write ("echo python3 Test.py "+ contractname + " "+ file+ "'\n'")
                            commands.write (Truffle_maker + "\n")
                            commands.write ("echo '"+ILF_bash_run + "'\n'")
                            commands.write (Truffle_maker + "\n")
                            commands.write ('read -p "Are you sure? " -n 1 -r choice' + ' \n\n\n\n\n')
    
                   
commands.close()