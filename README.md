<p align="center">
  <img src="resources/logo-full.svg" alt="FLock Logo" width="400" />
</p>

# Etherscan MCP Python Server

A complete Python implementation of the Etherscan Model Context Protocol (MCP) server, providing comprehensive access to Ethereum blockchain data through the Etherscan API.

## Overview

This server provides 56 comprehensive tools for accessing Ethereum blockchain data, including:

- **Account Tools**: Balance checking, transaction history, internal transactions
- **Block Tools**: Block data, rewards, timing information
- **Contract Tools**: Source code, ABI, verification status
- **Transaction Tools**: Transaction details, receipts, status
- **Token Tools**: Transfers, balances, supply information
- **Gas Tools**: Gas prices, estimates, oracle data
- **Statistics Tools**: Network metrics, supply data
- **RPC Tools**: Ethereum RPC proxy methods
- **Logs Tools**: Event logs and filtering

## Requirements

- Python 3.8+
- Etherscan API Key

## Installation

```bash
cd etherscan-mcp-python
pip install -e .
```

## Configuration

Set your Etherscan API key as an environment variable:

```bash
export ETHERSCAN_API_KEY="your_api_key_here"
```

Or create a `.env` file:
```bash
cp .env.example .env
# Edit .env and add your API key
```

## Usage

### Standalone Server
```bash
python server.py
```

### With MCP Tools (Agno Framework)
```python
from agno.tools.mcp import MCPTools

etherscan_mcp = MCPTools(
    command="python etherscan-mcp-python/server.py",
    env={"ETHERSCAN_API_KEY": "your_api_key"},
    timeout_seconds=120
)
```

## Testing Tools

To test all tools and generate recommendations for Agent development:

```bash
# Setup
cp .env.example .env
# Add your API key to .env file

# Run comprehensive test (tests all 56 tools)
python test_all_tools.py
```

This will test all 56 tools and generate:
- **tool_test_results.json**: Raw test results with performance metrics

## Complete Tool Reference

### 🏦 Account Tools (12 tools)
| Tool Name | Description | Key Parameters |
|-----------|-------------|----------------|
| `account_balance` | Get ETH balance for single address | `address`, `chainid` |
| `account_balancemulti` | Get ETH balance for multiple addresses (up to 20) | `address` (comma-separated), `chainid` |
| `account_txlist` | Get normal transactions by address | `address`, `startblock`, `endblock`, `page`, `offset` |
| `account_txlistinternal` | Get internal transactions by address | `address`, `startblock`, `endblock`, `page`, `offset` |
| `account_txlistinternal_byhash` | Get internal transactions by transaction hash | `txhash`, `chainid` |
| `account_txlistinternal_byblock` | Get internal transactions by block range | `startblock`, `endblock`, `page`, `offset` |
| `account_tokentx` | Get ERC20 token transfer events | `address`, `contractaddress`, `startblock`, `endblock` |
| `account_tokennfttx` | Get ERC721 (NFT) token transfer events | `address`, `contractaddress`, `startblock`, `endblock` |
| `account_token1155tx` | Get ERC1155 token transfer events | `address`, `contractaddress`, `startblock`, `endblock` |
| `account_fundedby` | Get address funding source and age | `address`, `chainid` |
| `account_getminedblocks` | Get blocks validated by address | `address`, `blocktype`, `page`, `offset` |
| `account_txsBeaconWithdrawal` | Get beacon chain withdrawals | `address`, `startblock`, `endblock`, `page`, `offset` |

### 🧱 Block Tools (4 tools)
| Tool Name | Description | Key Parameters |
|-----------|-------------|----------------|
| `block_getblockreward` | Get block mining reward and uncle rewards | `blockno`, `chainid` |
| `block_getblockcountdown` | Get estimated time until block is mined | `blockno`, `chainid` |
| `block_getblocknobytime` | Get block number by timestamp | `timestamp`, `closest`, `chainid` |
| `block_getblocktxnscount` | Get number of transactions in block | `blockno`, `chainid` |

### 📄 Contract Tools (4 tools)
| Tool Name | Description | Key Parameters |
|-----------|-------------|----------------|
| `contract_getabi` | Get contract ABI for verified contracts | `address`, `chainid` |
| `contract_getsourcecode` | Get verified contract source code | `address`, `chainid` |
| `contract_getcontractcreation` | Get contract creator and creation tx hash | `contractaddresses`, `chainid` |
| `contract_checkverifystatus` | Check contract verification status | `guid`, `chainid` |

### 🔄 Transaction Tools (2 tools)
| Tool Name | Description | Key Parameters |
|-----------|-------------|----------------|
| `transaction_getstatus` | Get contract execution status | `txhash`, `chainid` |
| `transaction_gettxreceiptstatus` | Get transaction receipt status | `txhash`, `chainid` |

### 🪙 Token Tools (2 tools)
| Tool Name | Description | Key Parameters |
|-----------|-------------|----------------|
| `stats_tokensupply` | Get ERC20 token total supply | `contractaddress`, `chainid` |
| `account_tokenbalance` | Get ERC20 token balance of address | `contractaddress`, `address`, `chainid` |

### ⛽ Gas Tools (3 tools)
| Tool Name | Description | Key Parameters |
|-----------|-------------|----------------|
| `gas_gasestimate` | Get estimated confirmation time for gas price | `gasprice`, `chainid` |
| `gas_gasoracle` | Get current safe/proposed/fast gas prices | `chainid` |
| `stats_dailyavggaslimit` | Get historical daily average gas limit | `startdate`, `enddate`, `sort`, `chainid` |

### 📊 Statistics Tools (13 tools)
| Tool Name | Description | Key Parameters |
|-----------|-------------|----------------|
| `stats_ethsupply` | Get total ETH supply (excluding staking/burnt) | `chainid` |
| `stats_ethsupply2` | Get total ETH supply (including staking/burnt) | `chainid` |
| `stats_ethprice` | Get current ETH price | `chainid` |
| `stats_chainsize` | Get blockchain size over date range | `startdate`, `enddate`, `clienttype`, `syncmode` |
| `stats_nodecount` | Get total discoverable nodes | `chainid` |
| `stats_dailytxnfee` | Get daily transaction fees paid to miners | `startdate`, `enddate`, `sort` |
| `stats_dailynewaddress` | Get daily new address count | `startdate`, `enddate`, `sort` |
| `stats_dailynetutilization` | Get daily network utilization percentage | `startdate`, `enddate`, `sort` |
| `stats_dailyavghashrate` | Get daily average network hash rate | `startdate`, `enddate`, `sort` |
| `stats_dailytx` | Get daily transaction count | `startdate`, `enddate`, `sort` |
| `stats_dailyavgnetdifficulty` | Get daily average mining difficulty | `startdate`, `enddate`, `sort` |
| `stats_ethdailyprice` | Get historical ETH prices | `startdate`, `enddate`, `sort` |

### 📝 Logs Tools (3 tools)
| Tool Name | Description | Key Parameters |
|-----------|-------------|----------------|
| `logs_getLogsByAddress` | Get event logs from address with block range | `address`, `fromBlock`, `toBlock`, `page`, `offset` |
| `logs_getLogsByTopics` | Get event logs filtered by topics | `fromBlock`, `toBlock`, `topic0-3`, operators |
| `logs_getLogsByAddressAndTopics` | Get event logs from address filtered by topics | `address`, `fromBlock`, `toBlock`, `topic0-3` |

### 🔗 RPC Proxy Tools (13 tools)
| Tool Name | Description | Key Parameters |
|-----------|-------------|----------------|
| `proxy_eth_blockNumber` | Get latest block number | `chainid` |
| `proxy_eth_getBlockByNumber` | Get block information by number | `tag`, `boolean`, `chainid` |
| `proxy_eth_getUncleByBlockNumberAndIndex` | Get uncle block by number and index | `tag`, `index`, `chainid` |
| `proxy_eth_getBlockTransactionCountByNumber` | Get transaction count in block | `tag`, `chainid` |
| `proxy_eth_getTransactionByHash` | Get transaction by hash | `txhash`, `chainid` |
| `proxy_eth_getTransactionByBlockNumberAndIndex` | Get transaction by block and index | `tag`, `index`, `chainid` |
| `proxy_eth_getTransactionCount` | Get transaction count by address | `address`, `tag`, `chainid` |
| `proxy_eth_getTransactionReceipt` | Get transaction receipt | `txhash`, `chainid` |
| `proxy_eth_call` | Execute message call without transaction | `to`, `data`, `tag`, `chainid` |
| `proxy_eth_getCode` | Get code at address | `address`, `tag`, `chainid` |
| `proxy_eth_getStorageAt` | Get storage value at position | `address`, `position`, `tag`, `chainid` |
| `proxy_eth_gasPrice` | Get current gas price | `chainid` |
| `proxy_eth_estimateGas` | Estimate gas for transaction | `data`, `to`, `value`, `gas`, `gasPrice` |

## 🤖 Essential Tools for Building Agents

*Based on comprehensive testing of all 55 tools using test_all_tools.py*

### Quick Reference for Agent Development

| Category | 🟢 Essential | 🟡 Situational | 🔴 Other Tools | Total |
|----------|-------------|----------------|-------------------|-------|
| **Account** | 11 tools | 1 tool | 0 tools | 12 tools |
| **Block** | 3 tools | 0 tools | 1 tool | 4 tools |
| **Contract** | 2 tools | 1 tool | 1 tool | 4 tools |
| **Transaction** | 2 tools | 0 tools | 0 tools | 2 tools |
| **Token** | 2 tools | 0 tools | 0 tools | 2 tools |
| **Gas** | 2 tools | 0 tools | 1 tool | 3 tools |
| **Statistics** | 3 tools | 0 tools | 9 tools | 12 tools |
| **Logs** | 0 tools | 3 tools | 0 tools | 3 tools |
| **RPC** | 12 tools | 0 tools | 1 tool | 13 tools |
| **TOTAL** | **37 tools** | **5 tools** | **13 tools** | **55 tools** |

#### Complete Essential Tools List

**Account Tools (11/12)**
- ✅ `account_balance` - Single ETH balance
- ✅ `account_balancemulti` - Multiple ETH balances
- ✅ `account_fundedby` - Funding source analysis
- ✅ `account_getminedblocks` - Blocks mined by address
- ✅ `account_token1155tx` - ERC-1155 token transfers
- ✅ `account_tokennfttx` - NFT transfers
- ✅ `account_txlist` - Normal transactions
- ✅ `account_txlistinternal` - Internal transactions
- ✅ `account_txlistinternal_byblock` - Internal tx by block range
- ✅ `account_txlistinternal_byhash` - Internal tx by hash
- ✅ `account_txsBeaconWithdrawal` - Beacon chain withdrawals

**Block Tools (4/4)**
- ✅ `block_getblocknobytime` - Block number by timestamp
- ✅ `block_getblockreward` - Block mining rewards
- ✅ `block_getblocktxnscount` - Transaction count in block
- ✅ `block_getblockcountdown` - Block countdown

**Contract Tools (3/4)**
- ✅ `contract_getcontractcreation` - Contract creation info
- ✅ `contract_getsourcecode` - Verified source code
- ✅ `contract_checkverifystatus` - Contract verification status

**Transaction Tools (2/2)**
- ✅ `transaction_getstatus` - Execution status
- ✅ `transaction_gettxreceiptstatus` - Receipt status

**Token Tools (2/2)**  
- ✅ `account_tokenbalance` - ERC-20 token balance
- ✅ `stats_tokensupply` - Total token supply

**Gas Tools (2/3)**
- ✅ `gas_gasestimate` - Gas time estimates
- ✅ `gas_gasoracle` - Current gas prices

**Statistics Tools (3/12)**
- ✅ `stats_chainsize` - Blockchain database size
- ✅ `stats_ethprice` - Current ETH price
- ✅ `stats_nodecount` - Network node count

**RPC Tools (12/13)**
- ✅ `proxy_eth_blockNumber` - Latest block number
- ✅ `proxy_eth_call` - Contract function call
- ✅ `proxy_eth_estimateGas` - Gas estimation
- ✅ `proxy_eth_gasPrice` - Current gas price
- ✅ `proxy_eth_getBlockByNumber` - Block details
- ✅ `proxy_eth_getBlockTransactionCountByNumber` - Block tx count
- ✅ `proxy_eth_getStorageAt` - Contract storage slot
- ✅ `proxy_eth_getTransactionByBlockNumberAndIndex` - Transaction by index
- ✅ `proxy_eth_getTransactionByHash` - Transaction details
- ✅ `proxy_eth_getTransactionCount` - Address nonce
- ✅ `proxy_eth_getTransactionReceipt` - Transaction receipt
- ✅ `proxy_eth_getUncleByBlockNumberAndIndex` - Uncle block data

### 🟡 Situational Tools (5 tools)
*Larger outputs, slower responses, or specific use cases - use carefully*

**Large Output Tools**
- ⚠️ `account_tokentx` - ERC-20 token transfers (use pagination for large datasets)

**Contract Analysis Tools**
- ⚠️ `contract_getabi` - Contract ABI (can be very large for complex contracts)

**Event Log Analysis Tools**
- ⚠️ `logs_getLogsByAddress` - Event logs by address 
- ⚠️ `logs_getLogsByTopics` - Event logs by topics
- ⚠️ `logs_getLogsByAddressAndTopics` - Combined filtering

**Usage Tips:**
- Use small block ranges for logs tools (1000 blocks max)  
- Implement pagination for transaction lists
- Cache results when possible
- Monitor response times and output sizes

### 🔴 Other Tools (11 tools)
*These tools failed during testing or require Pro accounts*

**Pro Account Required**
Most daily statistics tools require Etherscan Pro accounts:
- ❌ `stats_dailyavghashrate` - Daily average hashrate
- ❌ `stats_dailyavgnetdifficulty` - Daily mining difficulty
- ❌ `stats_dailynetutilization` - Daily network utilization
- ❌ `stats_dailynewaddress` - Daily new addresses
- ❌ `stats_dailytx` - Daily transaction count
- ❌ `stats_dailytxnfee` - Daily transaction fees
- ❌ `stats_ethdailyprice` - Historical ETH prices
- ❌ `stats_ethsupply` - ETH supply data
- ❌ `stats_ethsupply2` - ETH supply data v2
- ❌ `stats_dailyavggaslimit` - Daily average gas limit

**Large Output Tools**
- ❌ `proxy_eth_getCode` - Contract bytecode (can be extremely large)

**Recommendation**: Use essential tools for reliable agent performance. Pro tools may work with upgraded Etherscan accounts.

## 🎯 Use Cases & Examples

### Basic Balance Check
```python
# Get ETH balance for single address
account_balance(address="0x...", chainid="1")

# Get balances for multiple addresses (up to 20)
account_balancemulti(address="0x...,0x...,0x...", chainid="1")
```

### Transaction Analysis
```python
# Get transaction history for address
account_txlist(address="0x...", startblock="0", endblock="99999999")

# Get internal transactions (contract interactions)
account_txlistinternal(address="0x...", page="1", offset="100")
```

### Block Information
```python
# Get transaction count in specific block (like the web3_GAIA_test.py example)
block_getblocktxnscount(blockno="17000000", chainid="1")

# Get block mining rewards
block_getblockreward(blockno="17000000", chainid="1")
```

### Market Data
```python
# Get current ETH price
stats_ethprice(chainid="1")

# Get current gas prices
gas_gasoracle(chainid="1")
```

### Smart Contract Analysis
```python
# Get contract source code (if verified)
contract_getsourcecode(address="0x...", chainid="1")

# Get contract ABI
contract_getabi(address="0x...", chainid="1")
```

## 🔧 Advanced Configuration

### Multi-Chain Support
The server supports multiple Ethereum networks via the `chainid` parameter:
- `"1"` - Ethereum Mainnet (default)
- `"5"` - Goerli Testnet  
- `"11155111"` - Sepolia Testnet
- And other supported networks

### Error Handling
The server includes comprehensive error handling for:
- ❌ Missing API keys
- ❌ Invalid parameters
- ❌ API rate limits
- ❌ Network timeouts
- ❌ Malformed responses

### Performance Optimization
- ✅ Synchronous HTTP client for MCP compatibility
- ✅ Efficient JSON parsing and response formatting
- ✅ Proper timeout handling (120 seconds default)
- ✅ Memory-efficient tool registration

## 🔐 Security & Best Practices

### API Key Management
- Store `ETHERSCAN_API_KEY` in environment variables
- Never commit API keys to version control
- Use `.env` files for local development
- Rotate API keys regularly

### Rate Limiting
- Etherscan API has rate limits (free tier: 5 calls/sec)
- The server respects these limits
- Consider upgrading to Etherscan Pro for higher limits

### Data Validation
- All input parameters are validated
- API responses are checked for errors
- Malformed data is handled gracefully

## 🆘 Troubleshooting

### Common Issues

**❌ "ETHERSCAN_API_KEY not set"**
- Solution: Set the environment variable `export ETHERSCAN_API_KEY="your_key"`

**❌ "Connection closed" or "Runtime error"**
- Solution: Ensure you're not running in nested async context
- Check that the server.py uses synchronous `main()` function

**❌ "Tool not found"**
- Solution: Verify tool names use underscores (`account_balance` not `account/balance`)
- Check that tool renaming for Gemini compatibility is applied

**❌ "Timeout after 120 seconds"**
- Solution: Check internet connectivity and API key validity
- Verify Etherscan API is not experiencing outages

### Debug Mode
For debugging, you can modify the server to add verbose logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🤝 Contributing

### Adding New Tools
1. Choose appropriate tool category file (`src/tools/`)
2. Follow existing patterns for parameter validation
3. Add comprehensive docstrings
4. Test with actual API calls
5. Update this README with new tool documentation