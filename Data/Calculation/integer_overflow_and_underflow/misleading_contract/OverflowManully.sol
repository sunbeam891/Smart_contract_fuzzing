pragma solidity 0.4.25;

//based on not-so-smart-contract

contract Overflow {
    uint private sellerBalance=0;
    
  constructor() public{
      
  }
    
    function add(uint value) public returns (bool){
    	require(sellerBalance + value >= value);
        sellerBalance += value; 
    } 
}