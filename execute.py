from web3 import Web3
from eth_account import Account

# Ethereum node provider URL (Infura in this example)
INFURA_URL = 'https://eth-sepolia.g.alchemy.com/v2/YTg4XGDZmgtjMXggnHyrKLzeLUhQ4eiO'

# Your Ethereum account private key and address
PRIVATE_KEY = 'e70988a08cb793b15634ad838c3fb7be4056cef220ea521d42c5428a286f77f4'
ADDRESS = '0xF4a86386e0297E1D53Ece30541091dda8098Ead5'

# Recipient address where you want to send ETH
RECIPIENT_ADDRESS = '0x0f1f135Ef58FfE444c87f3674944947edB9D9B8E'

# Initialize Web3 instance
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

def execute_transaction(amount_eth):
    try:
        # Convert ETH amount to Wei (1 ETH = 10^18 Wei)
        amount_wei = web3.toWei(amount_eth, 'ether')

        # Fetch the current gas price from the network
        gas_price = web3.eth.gas_price

        # Build transaction
        transaction = {
            'to': RECIPIENT_ADDRESS,
            'value': amount_wei,
            'gas': 2000000,
            'gasPrice': gas_price,
            'nonce': web3.eth.get_transaction_count(ADDRESS),
            'chainId': 1,  # Replace with the correct chain ID if needed
        }

        # Sign transaction
        signed_tx = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

        # Send transaction
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

        print(f"Transaction sent. Hash: {web3.toHex(tx_hash)}")
        return web3.toHex(tx_hash)

    except Exception as e:
        print(f"Error in execute_transaction: {str(e)}")
        return None

# Example usage: Execute a transaction sending 0.1 ETH to the recipient address
if __name__ == "__main__":
    tx_hash = execute_transaction(0.1)
    if tx_hash:
        print(f"Transaction successful. Hash: {tx_hash}")
    else:
        print("Transaction failed.")
