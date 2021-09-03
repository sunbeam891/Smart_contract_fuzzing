#!/bin/bash


export TARGET=$1
export FUZZER=$2
export RUNS=$3

if [[ "x$TARGET" == "x" ]] || [[ "x$FUZZER" == "x" ]]
then
    echo "Usage: $0 TARGET FUZZER"
    exit 1
fi

#### Confuzzius ####
if [[ $FUZZER == "Confuzzius" ]] || [[ $FUZZER == "all" ]]
then 
    chmod +x common_file.sh
    ./common_file.sh saddie/confuzzius:script_edit_4 $TARGET $FUZZER results-Confuzzius $RUNS /root/
fi
#### ILF ####
if [[ $FUZZER == "ILF" ]] || [[ $FUZZER == "all" ]]
then 
    chmod +x common_file.sh
    ./common_file.sh saddie/ilf:script_edit_4 $TARGET $FUZZER results-ILF $RUNS /go/src/ilf/
fi


#### sFuzz ####
if [[ $FUZZER == "sFuzz" ]] || [[ $FUZZER == "all" ]]
then 
    chmod +x common_file.sh
    ./common_file.sh saddie/sfuzz:script_edit_5 $TARGET $FUZZER results-sFuzz $RUNS /home/sFuzz/build/fuzzer/
fi

