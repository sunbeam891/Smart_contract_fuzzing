pragma solidity ^0.4.2;

contract Caller {
    function callAddress(address a) {
        a.call();
    }
}