/*
 * @source: ChainSecurity
 * @author: Anton Permenev
 */
pragma solidity 0.4.26;

contract RuntimeUserInputCall{

    function check(address b){
        assert(B(b).foo() == 10);
    }

}

contract B{
    function foo() returns(uint);
}
