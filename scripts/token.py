#!/usr/bin/python3

from brownie import HuskyToken, accounts


def main():
    return HuskyToken.deploy("Husky", "HUSKY", 1e21, {'from': accounts[0]})
