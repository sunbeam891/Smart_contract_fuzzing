pragma solidity 0.4.26;

contract OutOfBoundsException {

	uint256[] private array;

	function getArrayElement(uint256 idx) public returns (uint256) {
		return array[idx];
	}

}
