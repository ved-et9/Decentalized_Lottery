from brownie import lottery,network,accounts,config
from scripts.deploy_lottery import deploy_lottery


def test_get_entry_fee():
    lottery = deploy_lottery()
    # assert lottery1.get_entry_fee() > Web3.to_wei(0.018,"ether")
    # assert lottery1.get_entry_fee() < Web3.to_wei(0.022,"ether")


#unit test is the smallest piece of code to be tested