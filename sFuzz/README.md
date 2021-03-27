# sFuzz 
## Implementation and setup 

### Docker method

Pull Docker image:

` docker pull sfuzz/ethfuzzer '

Run the container and map ` contracts/ ` folder to the container:

` docker run -it -v /path/to/contracts/folder/:/home/contracts/ sfuzz/ethfuzzer `

Note: "/path/to/contracts/folder" is the path to contracts folder inside the docker container.

Test the Solidity smart contract from the contracts folder: 

` cd /home/ && ./fuzzer -g -r 0 -d 120 && chmod +x fuzzMe && ./fuzzMe `
