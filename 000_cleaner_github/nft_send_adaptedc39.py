from web3 import Web3, Account
import json
import time
from time import sleep

# Connect to Ethereum node
infura_url = "YOUR_RPC_PROVIDER"
web3 = Web3(Web3.HTTPProvider(infura_url))

if not web3.is_connected():
    print("Failed to connect to Ethereum network")
    exit()

# Contract address and ABI
nft_contract_address = "0x4D97DCd97eC945f40cF65F87097ACe5EA0476045"

# Load ABI from file
with open('abi.json', 'r') as f:
    abi = json.load(f)

erc1155_abi = abi  # Replace with the ERC-1155 ABI

# Create contract instance
nft_contract = web3.eth.contract(address=nft_contract_address, abi=erc1155_abi)

# Wallet details#

sender_private_key = "YOUR_PRIVATE_KEY" # C40

sender_account = Account.from_key(sender_private_key)
sender_address = sender_account.address

# Recipient address
recipient_address = "FRONTEND_ADDRESS"

# Load token list and sizes from assetandsize.json
try:
    with open('assetandsize.json', 'r') as f:
        asset_data = json.load(f)
    print(f"Loaded {len(asset_data)} tokens from assetandsize.json")
except FileNotFoundError:
    print("Error: assetandsize.json file not found. Please run the Polymarket extractor first.")
    exit()
except json.JSONDecodeError:
    print("Error: Invalid JSON format in assetandsize.json")
    exit()

if not asset_data:
    print("No tokens found in assetandsize.json")
    exit()

# Process each token from the JSON file
for token_id_str, size in asset_data.items():
    try:
        # Convert token_id from string to int
        token_id = int(token_id_str)

        # Calculate token_amount (size * 1000000)
        token_amount = int(size * 1000000)

        print(f"Processing token {token_id} with amount {token_amount} (size: {size})")

        # Build the transaction
        transaction = nft_contract.functions.safeTransferFrom(
            sender_address,
            recipient_address,
            token_id,
            token_amount,  # size * 1000000
            b''  # Additional data (optional)
        ).build_transaction({
            'chainId': 137,  # Polygon Mainnet
            'gas': 400000,  # Adjust gas limit as needed
            'gasPrice': web3.to_wei('200', 'gwei'),  # Adjust gas price as needed
            'nonce': web3.eth.get_transaction_count(sender_address),
        })

        # Sign the transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=sender_private_key)

        # Send the transaction
        txn_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)

        # Wait for the transaction to be mined
        txn_receipt = web3.eth.wait_for_transaction_receipt(txn_hash)
        print(f"Transaction successful with hash: {txn_hash.hex()}")
        print(f"Transferred {size} shares (token_amount: {token_amount}) of token {token_id}")
        sleep(3)

    except ValueError as e:
        print(f"Error converting token_id or size for {token_id_str}: {e}")
        continue
    except Exception as e:
        print(f"Error processing token {token_id_str}: {e}")
        continue

print("All transfers completed!")
