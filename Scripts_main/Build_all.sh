#!/bin/bash

#export NO_CACHE="--no-cache"
#export MAKE_OPT="-j4"

cd $PFBENCH

cd Scripts_main

chmod +x requirements_install.sh

./requirements_install.sh

docker pull saddie/confuzzius:script_edit_4

docker pull saddie/ilf:script_edit_4

docker pull saddie/sfuzz_build:latest