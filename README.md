# MEV-BOT

Demo Video of the project is available here: https://www.youtube.com/watch?v=2sK-dtYF2-k&feature=youtu.be


# Automated Cryptocurrency Trading Bot

This project is an automated trading bot that detects volume surges in cryptocurrency markets and executes buy orders on the Ethereum Sepolia testnet.

## Features

- **Volume Surge Detection**: Monitors token trading volume for significant increases.
- **Automated Trading**: Executes buy orders automatically upon detecting a volume surge.
- **Real-Time Data**: Fetches up-to-date trading data using the Bitquery API.
- **Blockchain Interaction**: Uses Web3.py to interact with the Ethereum blockchain.

## Technologies Used

- Python
- Bitquery API
- Web3.py
- Infura

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/trading-bot.git
    cd trading-bot
    ```

2. **Install the required libraries**:
    ```bash
    pip install requests
    pip install web3
    ```

3. **Configure environment variables**:
    Create a `.env` file in the project directory and add the following:
    ```env
    BITQUERY_AUTH_TOKEN=your_bitquery_auth_token
    INFURA_URL=https://eth-sepolia.g.alchemy.com/v2/your_infura_key
    PRIVATE_KEY=your_private_key
    ADDRESS=your_wallet_address
    ```

## Usage

1. **Update the configuration**:
   - Edit `TOKEN_ADDRESS`, `VOLUME_SURGE_THRESHOLD`, and `TIME_WINDOW_MINUTES` in the script as needed.

2. **Run the bot**:
    ```bash
    python bot.py
    ```

The bot will monitor trading volume and execute buy orders when a surge is detected.

---

Feel free to customize this as needed for your specific project details!