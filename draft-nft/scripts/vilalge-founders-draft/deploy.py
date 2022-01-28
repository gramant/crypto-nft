#!/usr/bin/python3
import os
from brownie import VillageFoundersDraft, accounts, network, config


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    publish_source = True if os.getenv("ETHERSCAN_TOKEN") else False
    VillageFoundersDraft.deploy({"from": dev}, publish_source=publish_source)
