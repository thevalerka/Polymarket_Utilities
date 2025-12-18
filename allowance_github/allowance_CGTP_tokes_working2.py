from web3 import Web3

# Connect to Ethereum network (Infura, Alchemy, local node, etc.)
web3 = Web3(Web3.HTTPProvider('YOUR_RPC_PROVIDER'))

# Your account's private key (DO NOT hardcode in production)
private_key = "YOUR_PRIVATE_KEY"

# Create account from private key using the updated method
account = web3.eth.account.from_key(private_key)


# ERC-20 token contract address and ABI2
erc20_contract_address = "0x4D97DCd97eC945f40cF65F87097ACe5EA0476045"
erc20_approve = """[{"constant": false,"inputs": [{"name": "_spender","type": "address" },{ "name": "_value", "type": "uint256" }],"name": "approve","outputs": [{ "name": "", "type": "bool" }],"payable": false,"stateMutability": "nonpayable","type": "function"}]"""
erc1155_set_approval = """[{"inputs": [{ "internalType": "address", "name": "operator", "type": "address" },{ "internalType": "bool", "name": "approved", "type": "bool" }],"name": "setApprovalForAll","outputs": [],"stateMutability": "nonpayable","type": "function"}]"""
abi_token = '[{"constant":true,"inputs":[{"name":"owner","type":"address"},{"name":"id","type":"uint256"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"collateralToken","type":"address"},{"name":"parentCollectionId","type":"bytes32"},{"name":"conditionId","type":"bytes32"},{"name":"indexSets","type":"uint256[]"}],"name":"redeemPositions","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"},{"name":"","type":"uint256"}],"name":"payoutNumerators","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"ids","type":"uint256[]"},{"name":"values","type":"uint256[]"},{"name":"data","type":"bytes"}],"name":"safeBatchTransferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"collateralToken","type":"address"},{"name":"collectionId","type":"bytes32"}],"name":"getPositionId","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"owners","type":"address[]"},{"name":"ids","type":"uint256[]"}],"name":"balanceOfBatch","outputs":[{"name":"","type":"uint256[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"collateralToken","type":"address"},{"name":"parentCollectionId","type":"bytes32"},{"name":"conditionId","type":"bytes32"},{"name":"partition","type":"uint256[]"},{"name":"amount","type":"uint256"}],"name":"splitPosition","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"oracle","type":"address"},{"name":"questionId","type":"bytes32"},{"name":"outcomeSlotCount","type":"uint256"}],"name":"getConditionId","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"parentCollectionId","type":"bytes32"},{"name":"conditionId","type":"bytes32"},{"name":"indexSet","type":"uint256"}],"name":"getCollectionId","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"collateralToken","type":"address"},{"name":"parentCollectionId","type":"bytes32"},{"name":"conditionId","type":"bytes32"},{"name":"partition","type":"uint256[]"},{"name":"amount","type":"uint256"}],"name":"mergePositions","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"operator","type":"address"},{"name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"questionId","type":"bytes32"},{"name":"payouts","type":"uint256[]"}],"name":"reportPayouts","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"conditionId","type":"bytes32"}],"name":"getOutcomeSlotCount","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"oracle","type":"address"},{"name":"questionId","type":"bytes32"},{"name":"outcomeSlotCount","type":"uint256"}],"name":"prepareCondition","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"}],"name":"payoutDenominator","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"owner","type":"address"},{"name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"id","type":"uint256"},{"name":"value","type":"uint256"},{"name":"data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"conditionId","type":"bytes32"},{"indexed":true,"name":"oracle","type":"address"},{"indexed":true,"name":"questionId","type":"bytes32"},{"indexed":false,"name":"outcomeSlotCount","type":"uint256"}],"name":"ConditionPreparation","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"conditionId","type":"bytes32"},{"indexed":true,"name":"oracle","type":"address"},{"indexed":true,"name":"questionId","type":"bytes32"},{"indexed":false,"name":"outcomeSlotCount","type":"uint256"},{"indexed":false,"name":"payoutNumerators","type":"uint256[]"}],"name":"ConditionResolution","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"stakeholder","type":"address"},{"indexed":false,"name":"collateralToken","type":"address"},{"indexed":true,"name":"parentCollectionId","type":"bytes32"},{"indexed":true,"name":"conditionId","type":"bytes32"},{"indexed":false,"name":"partition","type":"uint256[]"},{"indexed":false,"name":"amount","type":"uint256"}],"name":"PositionSplit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"stakeholder","type":"address"},{"indexed":false,"name":"collateralToken","type":"address"},{"indexed":true,"name":"parentCollectionId","type":"bytes32"},{"indexed":true,"name":"conditionId","type":"bytes32"},{"indexed":false,"name":"partition","type":"uint256[]"},{"indexed":false,"name":"amount","type":"uint256"}],"name":"PositionsMerge","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"redeemer","type":"address"},{"indexed":true,"name":"collateralToken","type":"address"},{"indexed":true,"name":"parentCollectionId","type":"bytes32"},{"indexed":false,"name":"conditionId","type":"bytes32"},{"indexed":false,"name":"indexSets","type":"uint256[]"},{"indexed":false,"name":"payout","type":"uint256"}],"name":"PayoutRedemption","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"operator","type":"address"},{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"id","type":"uint256"},{"indexed":false,"name":"value","type":"uint256"}],"name":"TransferSingle","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"operator","type":"address"},{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"ids","type":"uint256[]"},{"indexed":false,"name":"values","type":"uint256[]"}],"name":"TransferBatch","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"operator","type":"address"},{"indexed":false,"name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"value","type":"string"},{"indexed":true,"name":"id","type":"uint256"}],"name":"URI","type":"event"}]'


erc20_abi = ''

# Initialize the ERC-20 contractzzzz
erc20_contract = web3.eth.contract(address=erc20_contract_address, abi=abi_token)

# Spender's address (who will spend the tokens)234ultddd
spender_address = "0xC5d563A36AE78145C45a50134d48A1215220f80a"

# Amount to approve (in smallest units, e.g., Wei for ETH-based tokens)
# If your token has 18 decimals, use web3.toWei() to convert to smallest units
amount_to_approve = web3.to_wei(1000000000, 'ether')  # Approving 100 tokens

# Get the transaction nonce (number of transactions sent from the account)
nonce = web3.eth.get_transaction_count(account.address)

# Build the transaction for the approve function
transaction = erc20_contract.functions.setApprovalForAll(
    spender_address,
    True
).build_transaction({
    'chainId': 137,  # Mainnet chain ID. Use 3 for Ropsten, 4 for Rinkeby, etc.
    'gas': 200000,  # Gas limit
    'gasPrice': web3.to_wei('1250', 'gwei'),  # Gas price
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
