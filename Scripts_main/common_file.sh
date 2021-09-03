#!/bin/bash
set -x
DOCIMAGE=$1   #name of the docker image
TARGET=$2
FUZZER=$3 
SAVETO=$4        
RUNS=$5 
ROOT=$6
#keep all container ids
cids=()

#create one container for each run
for i in $(seq 1 $RUNS); do
  id=$(docker run --cpus=1 -v ${TARGET}:${ROOT}dataset -d -it $DOCIMAGE /bin/bash -c "cd ${ROOT}dataset && chmod +x fuzzer_run.sh && ./fuzzer_run.sh ${FUZZER} ${ROOT}dataset ${ROOT} ${i} ${SAVETO}") # i used for determining container number for output file name
  cids+=(${id::12}) #store only the first 12 characters of a container ID
done

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
printf "\n${FUZZER^^}: Collected results and saved them to ${SAVETO}"


printf "\n${FUZZER^^}: I am done!"
