pragma solidity ^0.4.2;

contract IntegerOverflowMinimal {
    uint public count = 1;

    function run(uint256 input) public {
        // <yes> <report> ARITHMETIC
        count -= input;
    }
}
