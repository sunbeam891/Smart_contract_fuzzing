pragma solidity ^0.4.2;

contract Overflow_Add {
    uint public balance = 1;

    function add(uint256 deposit) public {
        // <yes> <report> ARITHMETIC
        balance += deposit;
    }
}
