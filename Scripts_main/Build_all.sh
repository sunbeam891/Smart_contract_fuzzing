#!/bin/bash

#export NO_CACHE="--no-cache"
#export MAKE_OPT="-j4"

cd $PFBENCH

cd Scripts_main

sudo chmod +x Requirements_install.sh

sudo ./requirements_install.sh

sudo docker pull saddie/confuzzius:script_edit_6

sudo docker pull saddie/ilf:script_edit_6

sudo docker pull saddie/sFuzz:script_edit_5