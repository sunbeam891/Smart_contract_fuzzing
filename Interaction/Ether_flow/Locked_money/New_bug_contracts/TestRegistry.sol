pragma solidity ^0.4.2;

// This contract is only used for testing purposes.
contract TestRegistry {

  mapping(address => uint) public registry;

  function register(uint x) payable public {
    registry[msg.sender] = x;
  }

}