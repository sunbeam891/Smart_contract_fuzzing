pragma solidity 0.4.26;

//use bytes instead of byte[]

contract waste2{
	//The type byte[] is an array of bytes, but due to padding rules, it wastes 31 bytes of space for each element (except in storage). It is better to use the bytes type instead.
	byte[] private _secret;

	constructor() public{
		_secret = new byte[](8);
	}
}
