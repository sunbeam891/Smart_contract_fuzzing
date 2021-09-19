#script0.23___ Correcting contract not read mistake + sFuzz timeout

# Format: python3 test.py <Fuzzer> <datasetlocation> <rootdirectoryforrunningfuzzer (/root/)> <ID> <SAVETO FOLDER>
import os
import sys
import pandas as pd
#files = os.listdir(path)
word = "contract"
delim = " "
words= []
fuzzer = sys.argv[1]
datasetloc = sys.argv[2]
rootdirectory = sys.argv[3]
ID= sys.argv[4]
Saveto = sys.argv[5]
excel_loc= "All_combined_1.xlsx"
contractname=""
done_files = []
script_loc = rootdirectory+"scripts/"
if fuzzer == "Confuzzius":
    commands = open ("Confuzzius_commands"+ID+".sh","w")
    commands.write ("#!/bin/bash" + " \n")
    os.system("mkdir "+Saveto+"_"+ID+ " \n")
    os.system("mkdir "+script_loc+ " \n")
    os.system("cp -a scripts/. "+script_loc+ " \n")
    commands.write("cd "+  rootdirectory + " \n")
    df = pd.read_excel (r'All_combined_1.xlsx', engine='openpyxl')
    for i in range (0,len(df)):
        con_file = df["Contract File name"][i]
        con_name  =df["Contract Name"][i]
        for root, dirs, files in os.walk(datasetloc):
            for file in files:
                if file == con_file and not os.path.join(root, file)+ con_name in done_files:
                    done_files.append(os.path.join(root, file)+ con_name)
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
                    con_name = con_name.strip()
                    
                    
                    saving_folder_or = datasetloc+"/"+Saveto+"_"+ID+"/"+file+"_"+con_name
                    saving_folder = saving_folder_or
                    for k in range (0,100):
                        if not os.path.isdir(saving_folder):
                            saving_folder = saving_folder+"/"
                            break
                        else:
                            saving_folder = saving_folder_or +str(k)
                        
                
                    Confuzzius_bash_run= "python3 fuzzer/main.py -s " + os.path.join(root, file) +" -c "+ con_name+ " --solc v0.4.26 --evm byzantium -t 10"
                    Data_retriever = "python3 "+script_loc+"excel_maker.py " + file+ " " + con_name + " " + os.path.join(root, "vuln.txt") + " " + fuzzer + " "+ID+" "+rootdirectory
                    Plotter_cov = "python3 "+script_loc+"Cov_plotter.py "+ file + " "+con_name+" "+ saving_folder+" " + os.path.join(root, file) + " " +datasetloc+"/"+Saveto+"_"+ID+ " "+ ID +" "+ os.path.join(root, "vuln.txt")+ " "+fuzzer  
                    #print (Confuzzius_bash_run)
                    commands.write ("echo '"+"File name = "+file  + " Contract Name = " +con_name+ "'\n")
                    commands.write ("echo '"+Confuzzius_bash_run + "'\n")
                    commands.write ('touch coverage_json.json ' + "\n")
                    commands.write ('touch vuln_json.json '+ "\n")
                    commands.write (Confuzzius_bash_run + "\n")
                    commands.write (Data_retriever + "\n")
                    os.system("mkdir "+saving_folder+ " \n")
                    commands.write ("cp cov_per_time.json "+saving_folder+"cov_per_time.json"+ " \n")
                    commands.write ("cp trigger_time.json "+saving_folder+"trigger_time.json"+ " \n")
                    commands.write(Plotter_cov+ " \n")
                    commands.write ("rm coverage_json.json" + " \n")
                    commands.write("rm vuln_json.json" + " \n")
                    commands.write("rm cov_per_time.json"+ " \n")
                    commands.write("rm trigger_time.json"+" \n\n\n\n")
                    #commands.write ('read -p "Are you sure? " -n 1 -r choice' + ' \n\n\n\n\n')
                            
                            
elif fuzzer == "ILF":
    commands = open ("ILF_commands"+ID+".sh","w")
    commands.write ("#!/bin/bash" + " \n")
    os.system("mkdir "+Saveto+"_"+ID+ " \n")
    os.system("mkdir "+script_loc+ " \n")
    os.system("cp -a scripts/. "+script_loc+ " \n")
    commands.write("cd "+  rootdirectory + " \n")
    df = pd.read_excel (r'All_combined_1.xlsx', engine='openpyxl')
    for i in range (0,len(df)):
        con_file = df["Contract File name"][i]
        con_name  =df["Contract Name"][i] 
        for root, dirs, files in os.walk(datasetloc):
            for file in files:
                if file == con_file and not os.path.join(root, file)+ con_name in done_files:
                    done_files.append(os.path.join(root, file)+ con_name)
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
                    con_name = con_name.strip()
                    saving_folder_or = datasetloc+"/"+Saveto+"_"+ID+"/"+file+"_"+con_name
                    saving_folder = saving_folder_or
                    for k in range (0,100):
                        if not os.path.isdir(saving_folder):
                            saving_folder = saving_folder+"/"
                            break
                        else:
                            saving_folder = saving_folder_or +str(k)

                    ILF_bash_run= "python3 -m ilf --proj ." + "/example/crowdsale" +" --contract "+ con_name+ " --fuzzer imitation --model ./model/ --limit 2000"
                    Truffle_maker= "python3 "+script_loc+"Truffle_maker.py "+ con_name + " "+ file
                    Data_retriever = "python3 "+script_loc+"excel_maker.py " + file+ " " + con_name + " " + os.path.join(root, "vuln.txt")+ " " + fuzzer + " "+ ID + " "+rootdirectory
                    Plotter_cov = "python3 "+script_loc+"Cov_plotter.py "+ file + " "+con_name+" "+ saving_folder+" " + os.path.join(root, file) + " " +datasetloc+"/"+Saveto+"_"+ID+ " "+ ID +" "+ os.path.join(root, "vuln.txt") + " "+fuzzer 
                    commands.write ("echo "+"File name = "+file  + " Contract Name = " +con_name+ "\n")
                    commands.write ("echo python3 Test.py "+ con_name + " "+ file+ "\n")
                    commands.write ('touch coverage_json.json ' + "\n")
                    commands.write ('touch vuln_json.json '+ "\n")
                    commands.write (Truffle_maker + "\n")
                    commands.write ("rm example/crowdsale/transactions.json" + " \n")
                    commands.write("python3 script/extract.py --proj example/crowdsale/ --port 8545 \n")
                    commands.write ("echo "+ILF_bash_run + "\n")
                    commands.write (ILF_bash_run + "\n")
                    commands.write (Data_retriever + "\n")
                    os.system("mkdir "+saving_folder+ " \n")
                    commands.write ("cp cov_per_time.json "+saving_folder+"cov_per_time.json"+ " \n")
                    commands.write ("cp trigger_time.json "+saving_folder+"trigger_time.json"+ " \n")
                    commands.write(Plotter_cov+ " \n")
                    commands.write ("rm coverage_json.json" + " \n")
                    commands.write("rm vuln_json.json" + " \n")
                    commands.write("rm cov_per_time.json"+ " \n")
                    commands.write("rm trigger_time.json"+" \n\n\n\n")
                    #commands.write ('read -p "Are you sure? " -n 1 -r choice' + ' \n\n\n\n\n')


elif fuzzer == "sFuzz":
    commands = open ("sFuzz_commands"+ID+".sh","w")
    commands.write ("#!/bin/bash" + " \n")
    os.system("mkdir "+Saveto+"_"+ID+ " \n")
    os.system("mkdir "+script_loc+ " \n")
    os.system("cp -a scripts/. "+script_loc+ " \n")
    commands.write("cd "+  rootdirectory + " \n")
    df = pd.read_excel (r'All_combined_1.xlsx', engine='openpyxl')
    for i in range (0,len(df)):
        con_file = df["Contract File name"][i]
        con_name  =df["Contract Name"][i] 
        for root, dirs, files in os.walk(datasetloc):
            for file in files:
                if file == con_file and not os.path.join(root, file)+ con_name in done_files:
                    done_files.append(os.path.join(root, file)+ con_name)
                    a_file= open(os.path.join(root, file),"r",encoding="utf-8")
                    #print(os.path.join(root, file))
                    listoflines=a_file.readlines()
                    for i in range (0,len(listoflines)):
                        s_line = listoflines[i].strip().split(" ")
                        if s_line[0] == "pragma":
                            listoflines[i] = "pragma solidity ^0.4.2;\n"
                    b_file=open(os.path.join(root, file),"w",encoding="utf-8")
                    b_file.writelines(listoflines)
                    b_file.close()
                    con_name = con_name.strip()
                    saving_folder_or = datasetloc+"/"+Saveto+"_"+ID+"/"+file+"_"+con_name
                    saving_folder = saving_folder_or
                    for k in range (0,100):
                        if not os.path.isdir(saving_folder):
                            saving_folder = saving_folder+"/"
                            break
                        else:
                            saving_folder = saving_folder_or +str(k)

                    sFuzz_bash_run= "./fuzzer -g -r 1 -d 120 && chmod +x fuzzMe && timeout 125 ./fuzzMe"
                    sFuzz_file_maker = "python3 "+script_loc+"sfuzz_file.py " + file + " " + con_name + " " + "contracts " + datasetloc
                    sFuzz_data_retriever = "python3 "+script_loc+"sfuzz_data_retr.py " +  con_name + ".sol"+" " + con_name + " " + "contracts/"
                    Data_retriever = "python3 "+ script_loc+"excel_maker.py " + file+ " " + con_name + " " + os.path.join(root, "vuln.txt")+ " " + fuzzer + " "+ID + " "+rootdirectory
                    sFuzz_per_time = "python3 "+script_loc+"sfuzz_per_time_retr.py "+ file + " "+ con_name + " "+ rootdirectory+"contracts"
                    Plotter_cov = "python3 "+script_loc+"Cov_plotter.py "+ file + " "+con_name+" "+ saving_folder+" " + os.path.join(root, file) + " " +datasetloc+"/"+Saveto+"_"+ID+ " "+ ID +" "+ os.path.join(root, "vuln.txt") + " "+fuzzer 
                    commands.write ("echo "+"File name = "+file  + " Contract Name = " +con_name+ "\n")
                    commands.write ("echo python3 Test.py "+ con_name + " "+ file+ "\n")
                    commands.write ('touch coverage_json.json ' + "\n")
                    commands.write ('touch vuln_json.json '+ "\n")
                    commands.write ("rm -rf contracts/" + "\n")
                    commands.write ("mkdir contracts" + "\n")
                    commands.write (sFuzz_file_maker + "\n")
                    #commands.write ("echo "+sFuzz_bash_run + "\n")
                    commands.write (sFuzz_bash_run + "\n")
                    commands.write (sFuzz_data_retriever + "\n")
                    commands.write (Data_retriever + "\n")
                    commands.write(sFuzz_per_time +" \n")
                    os.system("mkdir "+saving_folder+ " \n")
                    commands.write ("cp cov_per_time.json "+saving_folder+"cov_per_time.json"+ " \n")
                    commands.write ("cp trigger_time.json "+saving_folder+"trigger_time.json"+ " \n")
                    commands.write(Plotter_cov+ " \n")
                    commands.write ("rm coverage_json.json" + " \n")
                    commands.write("rm vuln_json.json" + " \n")
                    commands.write("rm cov_per_time.json"+ " \n")
                    commands.write("rm trigger_time.json"+" \n\n\n\n")
                    #commands.write ('read -p "Are you sure? " -n 1 -r choice' + ' \n\n\n\n\n')
    
                   
commands.close()