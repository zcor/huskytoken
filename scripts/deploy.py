#!/usr/bin/python3

from brownie import HuskyTokenDeployer, accounts, HuskyToken, HuskyTokenMinter, Wei
def main():
    provost = accounts.load('husky')
#    admin = '0x561369B3eC94D001031822011B9231e1436bcc78'
    admin = provost
    is_live = False
    if provost.balance() == 0:
        accounts[0].transfer(provost, Wei('1 ether'))
    husky_token = HuskyToken.deploy("Husky", "HUSKY", 0, {'from': provost}, publish_source=is_live)
    husky_token_minter = HuskyTokenMinter.deploy(husky_token, admin, {'from': provost}, publish_source=is_live)
    husky_token.addMinter(husky_token_minter, {'from': provost});
    husky_token.renounceMinter({'from': provost});

    #husky = HuskyTokenDeployer.deploy("Husky", "HUSKY", accounts[0], {'from': accounts[0]})
    
