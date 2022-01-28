#!/usr/bin/python3
from brownie import VillageFoundersDraft, accounts, network, config
from scripts.helpful_scripts import OPENSEA_FORMAT

def main(token_id, sample_token_uri):
    dev = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    test_nft = VillageFoundersDraft[len(VillageFoundersDraft) - 1]
    transaction = test_nft.setTokenURI(
        int(token_id),
        sample_token_uri, {"from": dev}
    )
    transaction.wait(1)
    print(
        "Awesome! You can view your NFT at {}".format(
            OPENSEA_FORMAT.format(test_nft.address, token_id)
        )
    )
    print('Please give up to 20 minutes, and hit the "refresh metadata" button')
