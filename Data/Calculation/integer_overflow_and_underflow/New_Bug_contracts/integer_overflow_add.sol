pragma solidity 0.4.26;

contract IntegerOverflowAdd {
    uint public count = 1;

    function run(uint256 input) public {
        // <yes> <report> ARITHMETIC
        count += input;
    }
}
