#Result_present.py V0.13, fixed errors
#Format = python3 Result_present.py <output_files> <output_folders> <Target dataset>
import os
import sys
import pandas as pd
import copy
import numpy as np
import math
import json
import matplotlib.pyplot as plt

arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]
all_combined = arg3+"All_combined_1.xlsx"
excel_files = arg1.split(',')[1:]
output_folders= arg2.split(',')[1:]

frame_name =""

dict_of_dfs = {}
fuzzer_names = []

for i,files in enumerate(excel_files):
    dataframe = pd.read_excel(arg3+"/"+files+".xlsx",header=None)
    dict_of_dfs[files]=copy.deepcopy(dataframe)
    fuzzer_names.append(files.split("-")[0])
Averaged_fuzzer={}


fuzzer_names = list(dict.fromkeys(fuzzer_names))
#print(fuzzer_names)
No_fuzzer_done = 0

for i in fuzzer_names:
    No_fuzzer_done = 0
    for k,files in enumerate(excel_files):
        dataframe = pd.read_excel(arg3+"/"+files+".xlsx",header=None)
        if i in files: 
            unique_vulns=[]
            if not i in Averaged_fuzzer.keys():
                Averaged_fuzzer[i]=copy.deepcopy(dataframe)
                Averaged_fuzzer[i][11]=np.nan
                for row in range(len(Averaged_fuzzer[i])):
                    Averaged_fuzzer[i][11][row] = ""
                    if Averaged_fuzzer[i][6][row] == "Yes":
                        unique_vulns.append(Averaged_fuzzer[i][4][row])
                    
                    if not Averaged_fuzzer[i][7][row] == "-":
                        if "," in str(Averaged_fuzzer[i][7][row]):
                            unique_vulns= unique_vulns + Averaged_fuzzer[i][7][row].split(",")
                        elif not str(Averaged_fuzzer[i][7][row]) == "nan":
                            unique_vulns.append(str(Averaged_fuzzer[i][7][row]))
                    if not len(unique_vulns)==0:
                        Averaged_fuzzer[i][11][row]=",".join(unique_vulns)
                    else:
                        Averaged_fuzzer[i][11][row]=""
                    unique_vulns=[]
                No_fuzzer_done = No_fuzzer_done+1 
            else:
                for j in range(len(dataframe)):
                    
                    #instruction coverage avg.
                    
                    if not  Averaged_fuzzer[i][2][j]=="-" and not isinstance(Averaged_fuzzer[i][2][j], float):
                        main_df_ins= float(Averaged_fuzzer[i][2][j].split(" ")[0].replace("%",""))
                    elif not  Averaged_fuzzer[i][2][j]=="-" and isinstance(Averaged_fuzzer[i][2][j], float):
                        main_df_ins = Averaged_fuzzer[i][2][j]
                    else:
                        main_df_ins=0
                    if not dataframe[2][j]=="-":
                        mean_df_ins= float(dataframe[2][j].split(" ")[0].replace("%",""))
                    else:
                        mean_df_ins=0
                    
                    
                    
                    #Branch Coverage
                    
                    if not Averaged_fuzzer[i][3][j]=="-" and not isinstance(Averaged_fuzzer[i][3][j], float):
                        main_df_br= float(Averaged_fuzzer[i][3][j].split(" ")[0].replace("%",""))
                    elif not  Averaged_fuzzer[i][3][j]=="-" and isinstance(Averaged_fuzzer[i][3][j], float):
                        main_df_br = Averaged_fuzzer[i][3][j]
                    else:
                        main_df_br=0
                    if not dataframe[3][j]=="-":
                        mean_df_br= float(dataframe[3][j].split(" ")[0].replace("%",""))
                    else:
                        mean_df_br=0
                    
                    
                    
                    #time taken average
                    
                    if not Averaged_fuzzer[i][9][j] == "-" and not isinstance(Averaged_fuzzer[i][9][j], float):
                        main_df_time= float(Averaged_fuzzer[i][9][j].split(" ")[0])
                    elif not  Averaged_fuzzer[i][9][j]=="-" and isinstance(Averaged_fuzzer[i][9][j], float):
                        main_df_time = Averaged_fuzzer[i][9][j]
                    else:
                        main_df_time=0
                    if not dataframe[9][j]=="-":
                        mean_df_time= float(dataframe[9][j].split(" ")[0])
                    else:
                        mean_df_time=0
                    
                    Averaged_fuzzer[i][2][j]=(((main_df_ins)*No_fuzzer_done)+mean_df_ins)/(No_fuzzer_done+1)
                    Averaged_fuzzer[i][3][j]=(((main_df_br)*No_fuzzer_done)+mean_df_br)/(No_fuzzer_done+1)
                    Averaged_fuzzer[i][9][j]=(((main_df_time)*No_fuzzer_done)+mean_df_time)/(No_fuzzer_done+1)
                    #print(Averaged_fuzzer[i][3][j])
                    
                    
                    #Unique Vulnerabilities
                    unique_vulns_add=[]
                    if dataframe[6][j] == "Yes":
                        Averaged_fuzzer[i][6][j]="Yes"
                        unique_vulns_add.append(dataframe[4][j])
                    
                    if not dataframe[7][j] == "-":
                        if "," in str(dataframe[7][j]):
                            unique_vulns_add= unique_vulns_add + dataframe[7][j].split(",")
                        elif not str(dataframe[7][j]) == "nan":
                            unique_vulns_add.append(str(dataframe[7][j]))
                    
                    if "," in str(Averaged_fuzzer[i][11][j]):
                        unique_vulns_add = list(set(str(Averaged_fuzzer[i][11][j]).split(",")+unique_vulns_add))
                    elif not Averaged_fuzzer[i][11][j] == "":
                        unique_vulns_add.append(Averaged_fuzzer[i][11][j])
                        unique_vulns_add = list(set(unique_vulns_add))
                    else:
                        unique_vulns_add = unique_vulns_add
                    
                    if not len(unique_vulns_add) == 0:
                        Averaged_fuzzer[i][11][j]=",".join(unique_vulns_add)
                    else:
                        Averaged_fuzzer[i][11][j]=""
                    unique_vulns_add=[]
                Averaged_fuzzer[i].to_excel("averaged_"+i+"_"+str(No_fuzzer_done)+".xlsx")
                No_fuzzer_done = No_fuzzer_done+1 
                    
                    
                  
                    

    
    
    
# Performance metrics : True Positives, False positives, not able to run, total unique vulns

perf_metrics = {}
fuzzer_avg_inst_cov=[]
fuzzer_ins_plot=[]
fuzzer_avg_branch_cov = []
fuzzer_branch_plot=[]
fuzzer_avg_time=[]
Performance_metrics= {}
for i in fuzzer_names:
    Performance_metrics[i]={}

for i in fuzzer_names:
    
    #Unique Vulns
    no_unique = 0
    no_true_pos = 0
    no_false_neg = 0
    no_able_run=0
    for row in range(len(Averaged_fuzzer[i])):
        for j,vulns in enumerate (Averaged_fuzzer[i][11][row].split(",")):
            if not vulns== "":
                no_unique=no_unique+1
     
    #True Positives
        if  Averaged_fuzzer[i][6][row]=="Yes":
            no_true_pos=no_true_pos+1
        
    #False negatives
        if  Averaged_fuzzer[i][6][row]=="No":
            no_false_neg = no_false_neg+1
            
    #Not_able_to_run
        
        if  Averaged_fuzzer[i][2][row] == 0.0 and Averaged_fuzzer[i][3][row] == 0.0:
            no_able_run=no_able_run+1
    
    Performance_metrics[i]["Unique_vulns"]=no_unique
    Performance_metrics[i]["True_pos"] = no_true_pos
    Performance_metrics[i]["Fals_neg"]= no_false_neg    
    Performance_metrics[i]["Not_able"] = no_able_run
    Performance_metrics[i]["Recall"] = (no_true_pos)/(no_true_pos+no_false_neg)

  

    #Plot bar graph for average code coverage
    
    A=Averaged_fuzzer[i]
    
    A = A.replace(0, np.nan)
    if i!="sFuzz":
        fuzzer_avg_inst_cov.append(A[2].mean())
        fuzzer_ins_plot.append(i)
    if i!="ILF":
        fuzzer_avg_branch_cov.append(A[3].mean())
        fuzzer_branch_plot.append(i)
    fuzzer_avg_time.append(A[9].mean())
#Plot bar graph for average code coverage    
plt.figure(figsize=(4,3))
plt.subplot(1,2,1)
plt.bar(fuzzer_ins_plot,fuzzer_avg_inst_cov,color=["r","b"])

for i in range(len(fuzzer_avg_inst_cov)):
    plt.annotate("{:.2f}".format(float(fuzzer_avg_inst_cov[i])), xy=(fuzzer_ins_plot[i],fuzzer_avg_inst_cov[i]), ha='center', va='bottom')
plt.savefig(arg3+"/Final_results/Average_inst_cov.png")    


#Plot bar graph for average branch coverage 
plt.subplot(1,2,2)
plt.bar(fuzzer_branch_plot,fuzzer_avg_branch_cov,color=["b","g"])    
for i in range(len(fuzzer_avg_branch_cov)):
    plt.annotate("{:.2f}".format(float(fuzzer_avg_branch_cov[i])), xy=(fuzzer_branch_plot[i],fuzzer_avg_branch_cov[i]), ha='center', va='bottom')


plt.savefig(arg3+"/Final_results/Average_bran_cov.png")    
    
plt.show()
plt.close()

with open(arg3+"/Final_results/Overall_performance.json", 'w', encoding="utf-8") as file:
    x = json.dumps(Performance_metrics, indent=4)
    file.write(x + '\n')  



# Display Average based on Vuln classification and display true positives 

Average_class_type= {}

vulns_class= ["Data","Description","Environment","Interaction","Interface","Logic","Performance","Security","Standard"]
Average_class_type = {"Code_cov":{},"time_taken":{}}

for fuzzer in fuzzer_names:
    Average_class_type["Code_cov"][fuzzer]={}
    Average_class_type["time_taken"][fuzzer]={}
for fuzzer in fuzzer_names:
    for vulnclass in vulns_class:
        Average_class_type["Code_cov"][fuzzer][vulnclass]=0
        Average_class_type["time_taken"][fuzzer][vulnclass]=0


        
        
#Dictionary for True positives, unique bugs, false negatives and not able to run in each class of bug

Metrics_class_type = {"True_pos":{},"False_neg":{},"Unique_bugs":{},"Not_able":{},"Recall":{}}
for fuzzer in fuzzer_names:
    Metrics_class_type["True_pos"][fuzzer]={}
    Metrics_class_type["False_neg"][fuzzer]={}
    Metrics_class_type["Unique_bugs"][fuzzer]={}
    Metrics_class_type["Not_able"][fuzzer]={}
    Metrics_class_type["Recall"][fuzzer]={}

for fuzzer in fuzzer_names:
    for vulnclass in vulns_class:
        Metrics_class_type["True_pos"][fuzzer][vulnclass]=0
        Metrics_class_type["False_neg"][fuzzer][vulnclass]=0 
        Metrics_class_type["Unique_bugs"][fuzzer][vulnclass]=0   
        Metrics_class_type["Not_able"][fuzzer][vulnclass]=0 
        Metrics_class_type["Recall"][fuzzer][vulnclass]=0


Class_times={"Data":0,"Description":0,"Environment":0,"Interaction":0,"Interface":0,"Logic":0,"Performance":0,"Security":0,"Standard":0}        

        
done_fuzzers = []

for i in fuzzer_names:
    Done_folders = [] 
    done_locs = []
    done_rows =[]
    #print(Class_times)
    Class_times={"Data":0,"Description":0,"Environment":0,"Interaction":0,"Interface":0,"Logic":0,"Performance":0,"Security":0,"Standard":0}
    if not i in done_fuzzers:
        done_fuzzers.append(i)
        for row in range(len(Averaged_fuzzer[i])):
            if not row in done_rows:
                done_rows.append(row)
                if i == "ILF":
                    counter = 5
                elif i == "Confuzzius":
                    counter = 3
                else:
                    counter = 6
                
                for classes in vulns_class:
                    if Averaged_fuzzer[i][5][row] == classes:
                        Average_class_type["Code_cov"][i][classes]=((float(Average_class_type["Code_cov"][i][classes])*(Class_times[classes]))+float(Averaged_fuzzer[i][2][row]))/(Class_times[classes]+1)
                        Average_class_type["time_taken"][i][classes]=((float(Average_class_type["time_taken"][i][classes])*(Class_times[classes]))+float(Averaged_fuzzer[i][9][row]))/(Class_times[classes]+1)
                                
                        #Unique bugs
                        for l,vulns in enumerate (Averaged_fuzzer[i][11][row].split(",")):
                            if not vulns== "":
                                Metrics_class_type["Unique_bugs"][i][classes]= Metrics_class_type["Unique_bugs"][i][classes]+1
                        #True Pos
                        if  Averaged_fuzzer[i][6][row]=="Yes":
                            Metrics_class_type["True_pos"][i][classes]=Metrics_class_type["True_pos"][i][classes]+1
                        #False Negatives
                                
                        if  Averaged_fuzzer[i][6][row]=="No":
                            Metrics_class_type["False_neg"][i][classes]=Metrics_class_type["False_neg"][i][classes]+1
                        #Not able
                        if  Averaged_fuzzer[i][2][row] == 0.0 and Averaged_fuzzer[i][3][row] == 0.0:
                                Metrics_class_type["Not_able"][i][classes]=Metrics_class_type["Not_able"][i][classes]+1
                                
                        class_sel = classes
                        Class_times[class_sel]=Class_times[class_sel]+1
        
        for class_re in vulns_class:
            Metrics_class_type["Recall"][i][class_re] = (Metrics_class_type["True_pos"][i][class_re])/(Metrics_class_type["True_pos"][i][class_re]+Metrics_class_type["False_neg"][i][class_re])
            #print(Metrics_class_type["Recall"][i][class_re])
                            
#Identify total contracts in each class and each category of metrics

total_contracts_class = {}
for i in fuzzer_names:
    total_contracts_class[i]={}
for i in fuzzer_names:
    for classes in vulns_class:
        total_contracts_class[i][classes]=0
for i in fuzzer_names:
    for row in range(len(Averaged_fuzzer[i])):
        total_contracts_class[i][Averaged_fuzzer[i][5][row]] = total_contracts_class[i][Averaged_fuzzer[i][5][row]]+1
        
        
        
#Create Dictionary with percentage values of TP and FN
Metrics_class_type_perc = {"True_pos":{},"False_neg":{},"Not_able":{}}
for fuzzer in fuzzer_names:
    Metrics_class_type_perc["True_pos"][fuzzer]={}
    Metrics_class_type_perc["False_neg"][fuzzer]={}
    Metrics_class_type_perc["Not_able"][fuzzer]={}


for fuzzer in fuzzer_names:
    for vulnclass in vulns_class:
        Metrics_class_type_perc["True_pos"][fuzzer][vulnclass]=0
        Metrics_class_type_perc["False_neg"][fuzzer][vulnclass]=0 
        Metrics_class_type_perc["Not_able"][fuzzer][vulnclass]=0 


for i in fuzzer_names:
    for classes in vulns_class:
        Metrics_class_type_perc["True_pos"][i][classes] =(Metrics_class_type["True_pos"][i][classes]/total_contracts_class[i][classes])*100
        Metrics_class_type_perc["False_neg"][i][classes]=(Metrics_class_type["False_neg"][i][classes]/total_contracts_class[i][classes])*100
        Metrics_class_type_perc["Not_able"][i][classes]=(Metrics_class_type["Not_able"][i][classes]/total_contracts_class[i][classes])*100

        
#Display TP, FN, Recall and failed for each class

TP = pd.DataFrame(columns = fuzzer_names,index = vulns_class)
for i in fuzzer_names:
    y_tp = list(Metrics_class_type_perc["True_pos"][i].values())
    TP[i]=y_tp
ax_plot = TP.plot(kind='bar' , title='True positive', figsize=(6, 4))
ax_plot.figure.savefig(arg3+"/Final_results/True_positive_classes.png",bbox_inches='tight')

FN = pd.DataFrame(columns = fuzzer_names,index = vulns_class)
for i in fuzzer_names:
    y_fn = list(Metrics_class_type_perc["False_neg"][i].values())
    FN[i]=y_fn
bx_plot = FN.plot(kind='bar' , title='False negative', figsize=(6, 4))
bx_plot.figure.savefig(arg3+"/Final_results/False_negative_classes.png",bbox_inches='tight')

NA = pd.DataFrame(columns = fuzzer_names,index = vulns_class)
for i in fuzzer_names:
    y_na= list(Metrics_class_type_perc["Not_able"][i].values())
    NA[i]=y_na
ax_plot = NA.plot(kind='bar' , title='Failed to run', figsize=(6, 4))
ax_plot.figure.savefig(arg3+"/Final_results/Failed_classes.png",bbox_inches='tight')

Re = pd.DataFrame(columns = fuzzer_names,index = vulns_class)
for i in fuzzer_names:
    y_re= list(Metrics_class_type["Recall"][i].values())
    Re[i]=y_re
ax_plot = Re.plot(kind='bar' , title='Recall', figsize=(6, 4))    
ax_plot.figure.savefig(arg3+"/Final_results/Recall_classes.png",bbox_inches='tight')    
