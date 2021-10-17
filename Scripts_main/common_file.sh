#!/bin/bash

DOCIMAGE=$1   #name of the docker image
TARGET=$2
FUZZER=$3 
SAVETO=$4        
RUNS=$5 
ROOT=$6
#keep all container ids
cids=()
excelnames='Start'
outputnames='Start'
#create one container for each run
if [[ $FUZZER != "all" ]]
then
  for i in $(seq 1 $RUNS); do
    id=$(docker run --cpus=1 -v ${TARGET}:${ROOT}dataset -d -it --entrypoint='' $DOCIMAGE /bin/bash -c "cd ${ROOT}dataset/Scripts_main && chmod +x fuzzer_run.sh && ./fuzzer_run.sh ${FUZZER} ${ROOT}dataset ${ROOT} ${i} ${SAVETO}") # i used for determining container number for output file name 
    cids+=(${id::12}) #store only the first 12 characters of a container ID
    excelnames+=,${FUZZER}-${i}-output
    outputnames+=,${SAVETO}_${i}

  done
fi

if [[ $FUZZER == "all" ]]
then 
  for i in $(seq 1 $RUNS); do
    id=$(docker run --cpus=1 -v ${TARGET}:/home/sFuzz/dataset -d -it --entrypoint='' saddie/sFuzz:script_edit_5 /bin/bash -c "cd /home/sFuzz/dataset/Scripts_main && chmod +x fuzzer_run.sh && ./fuzzer_run.sh sFuzz /home/sFuzz/dataset /home/sFuzz/ ${i} results-sFuzz") # i used for determining container number for output file name 
    cids+=(${id::12}) #store only the first 12 characters of a container ID
    excelnames+=,sFuzz-${i}-output
    outputnames+=,results-sFuzz_${i}

  done
fi
if [[ $FUZZER == "all" ]]
then 
  for i in $(seq 1 $RUNS); do
    id=$(docker run --cpus=1 -v ${TARGET}:/go/src/ilf/dataset -d -it --entrypoint='' saddie/ILF:script_edit_6 /bin/bash -c "cd /go/src/ilf/dataset/Scripts_main && chmod +x fuzzer_run.sh && ./fuzzer_run.sh ILF /go/src/ilf/dataset /go/src/ilf/ ${i} results-ILF") # i used for determining container number for output file name 
    cids+=(${id::12}) #store only the first 12 characters of a container ID
    excelnames+=,ILF-${i}-output
    outputnames+=,results-ILF_${i}

  done
fi

if [[ $FUZZER == "all" ]]
then 
  for i in $(seq 1 $RUNS); do
    id=$(docker run --cpus=1 -v ${TARGET}:/root/dataset -d -it --entrypoint='' saddie/confuzzius:script_edit_6 -c "cd /root/dataset/Scripts_main && chmod +x fuzzer_run.sh && ./fuzzer_run.sh Confuzzius /root/dataset /root/ ${i} results-Confuzzius") # i used for determining container number for output file name 
    cids+=(${id::12}) #store only the first 12 characters of a container ID
    excelnames+=,Confuzzius-${i}-output
    outputnames+=,results-Confuzzius_${i}

  done
fi

dlist="" #docker list
for id in ${cids[@]}; do
  dlist+=" ${id}"
done

#wait until all these dockers are stopped
printf "\n${FUZZER^^}: Fuzzing in progress ..."
printf "\n${FUZZER^^}: Waiting for the following containers to stop: ${dlist}"
docker wait ${dlist} > /dev/null
wait

#collect the fuzzing results from the containers
printf "Collecting results and performing necessary operations ..... "
mkdir ${TARGET}/Final_results/
rid=$(python3 ${TARGET}/Scripts_main/Result_present.py ${excelnames} ${outputnames} ${TARGET})
wait $rid


printf "\n${FUZZER^^}: Collected results and saved them to ${TARGET}/Final_results/"


printf "\n${FUZZER^^}: I am done!"
