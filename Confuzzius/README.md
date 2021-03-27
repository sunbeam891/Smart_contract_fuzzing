# Confuzzius 
## Implementation and setup

### Docker method 
To pull the docker image: 

` docker pull christoftorres/confuzzius `

To run the docker image:

` docker run -i -t christoftorres/confuzzius `

Evaluate a smart contract and run the Confuzzius fuzzer on it:

` python3 fuzzer/main.py -s <**Location of Contract**> -c TokenSale --solc v0.4.26 --evm byzantium -t 10 `

Note: Location of smart contract should be within the docker container created. 
