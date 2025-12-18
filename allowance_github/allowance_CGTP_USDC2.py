from web3 import Web3
import time
from time import sleep

# Connect to Ethereum network (Infura, Alchemy, local node, etc.)
web3 = Web3(Web3.HTTPProvider('YOUR_RPC_PROVIDER'))

# Your account's private key (DO NOT hardcode in production)
private_key = "YOUR_PRIVATE_KEY"

# Create account from private key using the updated method
account = web3.eth.account.from_key(private_key)


# ERC-20 token contract address and ABIxxx
erc20_contract_address = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"
erc20_approve = """[{"constant": false,"inputs": [{"name": "_spender","type": "address" },{ "name": "_value", "type": "uint256" }],"name": "approve","outputs": [{ "name": "", "type": "bool" }],"payable": false,"stateMutability": "nonpayable","type": "function"}]"""
erc1155_set_approval = """[{"inputs": [{ "internalType": "address", "name": "operator", "type": "address" },{ "internalType": "bool", "name": "approved", "type": "bool" }],"name": "setApprovalForAll","outputs": [],"stateMutability": "nonpayable","type": "function"}]"""

erc20_abi = ''

# Initialize the ERC-20 contract
erc20_contract = web3.eth.contract(address=erc20_contract_address, abi=erc20_approve)


#--------------------------------------1--------------------------------------------------------------

# Spender's address (who will spend the tokens)234ult23
spender_address = "0xC5d563A36AE78145C45a50134d48A1215220f80a"

# Amount to approve (in smallest units, e.g., Wei for ETH-based tokens)
# If your token has 18 decimals, use web3.toWei() to convert to smallest units
amount_to_approve = web3.to_wei(1000000000000000, 'ether')  # Approving 100 tokens

# Get the transaction nonce (number of transactions sent from the account)
nonce = web3.eth.get_transaction_count(account.address)

# Build the transaction for the approve function
transaction = erc20_contract.functions.approve(
    spender_address,
    amount_to_approve
).build_transaction({
    'chainId': 137,  # Mainnet chain ID. Use 3 for Ropsten, 4 for Rinkeby, etc.xxx
    'gas': 300000,  # Gas limit
    'gasPrice': web3.to_wei('1280', 'gwei'),  # Gas pricexx
    'nonce': nonce,  # Account nonce
})

# Sign the transaction using the private key
signed_tx = web3.eth.account.sign_transaction(transaction, private_key=private_key)

# Send the transaction to the Ethereum network
tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)

# Get transaction hash and wait for receipt (optional)
print(f"Transaction hash: {tx_hash.hex()}")
receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Transaction receipt: {receipt}")
