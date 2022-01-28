## Prerequisites

Please install or have installed the following:

- [nodejs and npm](https://nodejs.org/en/download/)
```bash
sudo apt install nodejs
sudo apt install npm
```
- [python](https://www.python.org/downloads/)
## Installation

1. [Install Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html), if you haven't already. Here is a simple way to install brownie.

```bash
pip install eth-brownie
```

2. [Install ganache-cli](https://www.npmjs.com/package/ganache-cli)

```bash
npm install -g ganache-cli
```

If you want to be able to deploy to testnets, do the following.

4. Set your environment variables

Set your `WEB3_INFURA_PROJECT_ID`, and `PRIVATE_KEY` [environment variables](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html).

You can get a `WEB3_INFURA_PROJECT_ID` by getting a free trial of [Infura](https://infura.io/). At the moment, it does need to be infura with brownie. You can find your `PRIVATE_KEY` from your ethereum wallet like [metamask](https://metamask.io/).

You'll also need testnet rinkeby ETH and LINK. You can get LINK and ETH into your wallet by using the [rinkeby faucets located here](https://faucets.chain.link/rinkeby). If you're new to this, [watch this video.](https://www.youtube.com/watch?v=P7FX_1PePX0)

You can add your environment variables to the `.env` file:

```
export WEB3_INFURA_PROJECT_ID=<PROJECT_ID>
export PRIVATE_KEY=<PRIVATE_KEY>
```

Then, make sure your `brownie-config.yaml` has:

```
dotenv: .env
```

### NFT metadata
To create nft with metadata create json (from sample json in folder metadata) and upload it to pinata [Pinata](https://pinata.cloud/). Store ipfs link for uploaded token metadata. 

### Running Scripts

You'll need [testnet Rinkeby](https://faucet.rinkeby.io/) and [testnet LINK](https://rinkeby.chain.link/) in the wallet associated with your private key.

To compile nft contracts run:
```
brownie compile all
```

To deploy run:
```
brownie run scripts/vilalge-founders-draft/deploy.py --network rinkeby
```

To create token run:
```
brownie run scripts/vilalge-founders-draft/create.py main <ipfs link to token metadata> --network rinkeby
```

To deploy run:
```
brownie run scripts/vilalge-founders-draft/update.py main <int token id> <ipfs link to token metadata>--network rinkeby
```
