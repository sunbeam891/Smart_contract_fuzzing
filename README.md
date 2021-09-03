# Smart_contract_fuzzing

### Implementation of fuzzers on smart contracts

## Requirements

1. Docker is required for the fuzzers to be run
2. Linux/Ubuntu has been used for testing
3. Docker image containes required solc and python versions.

## Installation and setup (Currently only Cofuzzius is runnable on the entire dataset) (Linux)

### Step 0. (Cloning repository)

``` 
  git clone https://github.com/sunbeam891/Smart_contract_fuzzing.git 
  cd Smart_contract_fuzzing
  export PFBENCH=$(pwd)
```

### Step 1. (Setting up the required Fuzzers) 

#### Requirements and pulling of Docker images

``` 
  cd Scripts_main
  chmod +x Build_all.sh
  ./Build_all.sh
```


### Step 2. (Fuzzing contracts in the dataset)

```
cd Scripts_main
./exec_file.sh $PFBENCH Confuzzius 3  
```



#### NOTE : exec_file.sh is the main script that governs how many fuzzers are run at a time and what the target dataset is. 

Format of exec_file.sh -> ./exec_file.sh <Folder having target dataset> <Fuzzer to be run (Confuzzius)(ILF)(sFuzz)(all)> <No. of times each fuzzer should be run parallely>

### arguments of exec_file.sh
  1. Argument 1 -> Path of folder having target dataset
  2. Argument 2 -> Name of Fuzzer to be run. Either All can be selected to run all fuzzers or 1 fuzzer's name
  3. Argument 3 -> No. of times each fuzzer should be run


If permission error occurs because the repository is private, Please use following command after entering the git local repository of this project:

` Sudo chown -R <Username in linux> * `
