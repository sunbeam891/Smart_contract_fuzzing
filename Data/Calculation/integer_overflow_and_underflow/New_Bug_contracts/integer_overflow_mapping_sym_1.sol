pragma solidity ^0.4.2;

contract IntegerOverflowMappingSym1 {
    mapping(uint256 => uint256) map;

    function init(uint256 k, uint256 v) public {
        // <yes> <report> ARITHMETIC
        map[k] -= v;
    }
}
