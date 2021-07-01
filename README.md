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
```

### Step 1. (Setting up the required Fuzzers) 

#### Confuzzius

``` 
  sudo docker pull christoftorres/confuzzius
  docker run -i -t -v $(pwd)/Dataset:/root/Dataset  christoftorres/confuzzius
```

Note: The process of Fuzzer installation will be done through docker build files and not docker images being pulled this way in the final version with all the process automated using scripts just like profuzzbench. All the Fuzzers will be setup properly using the scripts in final version and user will be asked which fuzzer is to be run on the dataset.

### Step 2. (Fuzzing the entire Dataset using scripts created)

```
  cd dataset
  python3 Command_create.py Confuzzius /root/dataset /root/
  chmod +x Confuzzius_commands.sh
  ./Confuzzius_commands.sh
```

Note: All this process will be automated with the final version allowing all this to be done by just telling the tool which fuzzer is to be used including an option to use all of them and which dataset is to be fuzzed
