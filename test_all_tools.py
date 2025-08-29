#!/usr/bin/env python3
"""
Comprehensive test script for all Etherscan MCP tools.
Tests all 56 tools to determine which are essential for building Agents.

Setup:
1. Copy .env.example to .env
2. Add your Etherscan API key to .env file
3. Run: python test_all_tools.py
"""

import os
import sys
import json
import time
from datetime import datetime, timedelta
import traceback
from pathlib import Path

# Load environment variables from .env file
def load_env():
    """Load environment variables from .env file if it exists."""
    env_path = Path(__file__).parent / '.env'
    if env_path.exists():
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if line.startswith('export '):
                    line = line[7:].strip()
                if '=' not in line:
                    continue
                key, value = line.split('=', 1)
                value = value.strip().strip('"').strip("'")
                os.environ[key] = value
        print("⚠️  .env file not found. Please copy .env.example to .env and add your API key.")
        print("   Get your API key from: https://etherscan.io/apis")
        return False
    return True

# Load environment variables
if not load_env():
    sys.exit(1)

# Check if API key is set
if not os.getenv("ETHERSCAN_API_KEY") or os.getenv("ETHERSCAN_API_KEY") == "your_api_key_here":
    print("❌ ETHERSCAN_API_KEY not set in .env file")
    print("   Please add your API key to the .env file:")
    print("   ETHERSCAN_API_KEY=your_actual_api_key_here")
    sys.exit(1)

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import the utils API call function directly
from tools.utils import api_call

class ToolTester:
    def __init__(self):
        self.results = {}
        self.test_data = self._get_test_data()
        
    def _get_test_data(self):
        """Get test data for different scenarios."""
        return {
            # Well-known addresses
            'vitalik_address': '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045',
            'usdt_contract': '0xdac17f958d2ee523a2206206994597c13d831ec7',
            'uniswap_router': '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D',
            
            # Recent block numbers (approximate)
            'recent_block': '19000000',
            'older_block': '18000000',
            
            # Known transaction hashes
            'known_tx': '0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060',
            'recent_tx': '0xa1e8d6d9d1f1b1c1e1f1a1b1c1d1e1f1a1b1c1d1e1f1a1b1c1d1e1f1a1b1c1d1',
            
            # Time ranges
            'yesterday': (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'),
            'week_ago': (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d'),
            'today': datetime.now().strftime('%Y-%m-%d'),
        }

    def test_tool(self, tool_name, api_params):
        """Test a single tool by making direct API calls."""
        try:
            start_time = time.time()
            result = api_call(api_params)
            end_time = time.time()
            
            response_time = end_time - start_time
            result_str = str(result)
            output_length = len(result_str)
            
            # Truncate very long outputs for analysis
            sample_output = result_str[:1000] + "..." if output_length > 1000 else result_str
            
            return {
                'success': True,
                'output_length': output_length,
                'response_time': round(response_time, 2),
                'sample_output': sample_output,
                'full_output': result_str if output_length < 5000 else "TRUNCATED_DUE_TO_LENGTH",
                'error': None,
                'requires_pro': self._check_pro_requirement(result_str),
                'api_params': api_params
            }
            
        except Exception as e:
            error_str = str(e)
            traceback_str = traceback.format_exc()
            
            return {
                'success': False,
                'output_length': 0,
                'response_time': 0,
                'sample_output': None,
                'full_output': None,
                'error': error_str,
                'traceback': traceback_str,
                'requires_pro': self._check_pro_requirement(error_str),
                'api_params': api_params
            }

    def _check_pro_requirement(self, text):
        """Check if the response indicates a Pro account requirement."""
        pro_indicators = [
            'Max rate limit reached',
            'upgrade to premium',
            'rate limit exceeded',
            'premium account',
            'pro api'
        ]
        return any(indicator.lower() in text.lower() for indicator in pro_indicators)

    def run_all_tests(self):
        """Run tests for all tool categories."""
        
        print("🧪 Starting comprehensive tool testing...")
        if os.environ.get('ETHERSCAN_API_KEY'):
            print("Using ETHERSCAN_API_KEY from environment.")
        print("=" * 80)
        
        # Test each category
        self._test_account_tools()
        self._test_block_tools()
        self._test_contract_tools()
        self._test_transaction_tools()
        self._test_token_tools()
        self._test_gas_tools()
        self._test_stats_tools()
        self._test_logs_tools()
        self._test_rpc_tools()
        
        return self.results

    def _test_account_tools(self):
        """Test account-related tools."""
        print("\n🏦 Testing Account Tools...")
        
        account_tests = [
            {
                'name': 'account_balance',
                'params': {
                    'module': 'account',
                    'action': 'balance',
                    'address': self.test_data['vitalik_address'],
                    'chainid': '1'
                }
            },
            {
                'name': 'account_balancemulti',
                'params': {
                    'module': 'account',
                    'action': 'balancemulti',
                    'address': f"{self.test_data['vitalik_address']},{self.test_data['usdt_contract']}",
                    'chainid': '1'
                }
            },
            {
                'name': 'account_txlist',
                'params': {
                    'module': 'account',
                    'action': 'txlist',
                    'address': self.test_data['vitalik_address'],
                    'startblock': '0',
                    'endblock': '99999999',
                    'page': '1',
                    'offset': '10',
                    'sort': 'asc',
                    'chainid': '1'
                }
            },
            {
                'name': 'account_txlistinternal',
                'params': {
                    'module': 'account',
                    'action': 'txlistinternal',
                    'address': self.test_data['vitalik_address'],
                    'startblock': '0',
                    'endblock': '99999999',
                    'page': '1',
                    'offset': '10',
                    'sort': 'asc',
                    'chainid': '1'
                }
            },
            {
                'name': 'account_txlistinternal_byhash',
                'params': {
                    'module': 'account',
                    'action': 'txlistinternal',
                    'txhash': self.test_data['known_tx'],
                    'chainid': '1'
                }
            },
            {
                'name': 'account_txlistinternal_byblock',
                'params': {
                    'module': 'account',
                    'action': 'txlistinternal',
                    'startblock': self.test_data['older_block'],
                    'endblock': self.test_data['recent_block'],
                    'page': '1',
                    'offset': '10',
                    'sort': 'asc',
                    'chainid': '1'
                }
            },
            {
                'name': 'account_tokentx',
                'params': {
                    'module': 'account',
                    'action': 'tokentx',
                    'address': self.test_data['vitalik_address'],
                    'startblock': '0',
                    'endblock': '99999999',
                    'page': '1',
                    'offset': '10',
                    'sort': 'asc',
                    'chainid': '1'
                }
            },
            {
                'name': 'account_tokennfttx',
                'params': {
                    'module': 'account',
                    'action': 'tokennfttx',
                    'address': self.test_data['vitalik_address'],
                    'startblock': '0',
                    'endblock': '99999999',
                    'page': '1',
                    'offset': '10',
                    'sort': 'asc',
                    'chainid': '1'
                }
            },
            {
                'name': 'account_token1155tx',
                'params': {
                    'module': 'account',
                    'action': 'token1155tx',
                    'address': self.test_data['vitalik_address'],
                    'startblock': '0',
                    'endblock': '99999999',
                    'page': '1',
                    'offset': '10',
                    'sort': 'asc',
                    'chainid': '1'
                }
            },
            {
                'name': 'account_fundedby',
                'params': {
                    'module': 'account',
                    'action': 'fundedby',
                    'address': self.test_data['vitalik_address'],
                    'chainid': '1'
                }
            },
            {
                'name': 'account_getminedblocks',
                'params': {
                    'module': 'account',
                    'action': 'getminedblocks',
                    'address': self.test_data['vitalik_address'],
                    'blocktype': 'blocks',
                    'page': '1',
                    'offset': '10',
                    'chainid': '1'
                }
            },
            {
                'name': 'account_txsBeaconWithdrawal',
                'params': {
                    'module': 'account',
                    'action': 'txsBeaconWithdrawal',
                    'address': self.test_data['vitalik_address'],
                    'startblock': '0',
                    'endblock': '99999999',
                    'page': '1',
                    'offset': '100',
                    'sort': 'asc',
                    'chainid': '1'
                }
            }
        ]
        
        for test in account_tests:
            self._run_single_test('Account', test)

    def _test_block_tools(self):
        """Test block-related tools.""" 
        print("\n🧱 Testing Block Tools...")
        
        block_tests = [
            {
                'name': 'block_getblockreward',
                'params': {
                    'module': 'block',
                    'action': 'getblockreward',
                    'blockno': self.test_data['recent_block'],
                    'chainid': '1'
                }
            },
            {
                'name': 'block_getblockcountdown',
                'params': {
                    'module': 'block',
                    'action': 'getblockcountdown',
                    'blockno': str(int(self.test_data['recent_block']) + 1000),
                    'chainid': '1'
                }
            },
            {
                'name': 'block_getblocknobytime',
                'params': {
                    'module': 'block',
                    'action': 'getblocknobytime',
                    'timestamp': str(int(time.time()) - 86400),  # 1 day ago
                    'closest': 'before',
                    'chainid': '1'
                }
            },
            {
                'name': 'block_getblocktxnscount',
                'params': {
                    'module': 'proxy',
                    'action': 'eth_getBlockTransactionCountByNumber',
                    'tag': hex(int(self.test_data['recent_block'])),
                    'chainid': '1'
                }
            }
        ]
        
        for test in block_tests:
            self._run_single_test('Block', test)

    def _test_contract_tools(self):
        """Test contract-related tools."""
        print("\n📄 Testing Contract Tools...")
        
        contract_tests = [
            {
                'name': 'contract_getabi',
                'params': {
                    'module': 'contract',
                    'action': 'getabi',
                    'address': self.test_data['usdt_contract'],
                    'chainid': '1'
                }
            },
            {
                'name': 'contract_getsourcecode',
                'params': {
                    'module': 'contract',
                    'action': 'getsourcecode',
                    'address': self.test_data['usdt_contract'],
                    'chainid': '1'
                }
            },
            {
                'name': 'contract_getcontractcreation',
                'params': {
                    'module': 'contract',
                    'action': 'getcontractcreation',
                    'contractaddresses': self.test_data['usdt_contract'],
                    'chainid': '1'
                }
            },
            {
                'name': 'contract_checkverifystatus',
                'params': {
                    'module': 'contract',
                    'action': 'checkverifystatus',
                    'guid': 'test-guid-placeholder',  # This will likely fail as it needs a real GUID
                    'chainid': '1'
                }
            }
        ]
        
        for test in contract_tests:
            self._run_single_test('Contract', test)

    def _test_transaction_tools(self):
        """Test transaction-related tools."""
        print("\n🔄 Testing Transaction Tools...")
        
        tx_tests = [
            {
                'name': 'transaction_getstatus',
                'params': {
                    'module': 'transaction',
                    'action': 'getstatus',
                    'txhash': self.test_data['known_tx'],
                    'chainid': '1'
                }
            },
            {
                'name': 'transaction_gettxreceiptstatus',
                'params': {
                    'module': 'transaction',
                    'action': 'gettxreceiptstatus',
                    'txhash': self.test_data['known_tx'],
                    'chainid': '1'
                }
            }
        ]
        
        for test in tx_tests:
            self._run_single_test('Transaction', test)

    def _test_token_tools(self):
        """Test token-related tools."""
        print("\n🪙 Testing Token Tools...")
        
        token_tests = [
            {
                'name': 'stats_tokensupply',
                'params': {
                    'module': 'stats',
                    'action': 'tokensupply',
                    'contractaddress': self.test_data['usdt_contract'],
                    'chainid': '1'
                }
            },
            {
                'name': 'account_tokenbalance',
                'params': {
                    'module': 'account',
                    'action': 'tokenbalance',
                    'contractaddress': self.test_data['usdt_contract'],
                    'address': self.test_data['vitalik_address'],
                    'chainid': '1'
                }
            }
        ]
        
        for test in token_tests:
            self._run_single_test('Token', test)

    def _test_gas_tools(self):
        """Test gas-related tools."""
        print("\n⛽ Testing Gas Tools...")
        
        gas_tests = [
            {
                'name': 'gas_gasoracle',
                'params': {
                    'module': 'gastracker',
                    'action': 'gasoracle',
                    'chainid': '1'
                }
            },
            {
                'name': 'gas_gasestimate',
                'params': {
                    'module': 'gastracker',
                    'action': 'gasestimate',
                    'gasprice': '20000000000',
                    'chainid': '1'
                }
            },
            {
                'name': 'stats_dailyavggaslimit',
                'params': {
                    'module': 'stats',
                    'action': 'dailyavggaslimit',
                    'startdate': self.test_data['week_ago'],
                    'enddate': self.test_data['yesterday'],
                    'sort': 'asc',
                    'chainid': '1'
                }
            }
        ]
        
        for test in gas_tests:
            self._run_single_test('Gas', test)

    def _test_stats_tools(self):
        """Test statistics-related tools."""
        print("\n📊 Testing Statistics Tools...")
        
        stats_tests = [
            {
                'name': 'stats_ethsupply',
                'params': {
                    'module': 'stats',
                    'action': 'ethsupply',
                    'chainid': '1'
                }
            },
            {
                'name': 'stats_ethsupply2',
                'params': {
                    'module': 'stats',
                    'action': 'ethsupply2',
                    'chainid': '1'
                }
            },
            {
                'name': 'stats_ethprice', 
                'params': {
                    'module': 'stats',
                    'action': 'ethprice',
                    'chainid': '1'
                }
            },
            {
                'name': 'stats_chainsize',
                'params': {
                    'module': 'stats',
                    'action': 'chainsize',
                    'startdate': self.test_data['week_ago'],
                    'enddate': self.test_data['yesterday'],
                    'clienttype': 'geth',
                    'syncmode': 'default',
                    'chainid': '1'
                }
            },
            {
                'name': 'stats_nodecount',
                'params': {
                    'module': 'stats',
                    'action': 'nodecount',
                    'chainid': '1'
                }
            },
            {
                'name': 'stats_dailytxnfee',
                'params': {
                    'module': 'stats',
                    'action': 'dailytxnfee',
                    'startdate': self.test_data['week_ago'],
                    'enddate': self.test_data['yesterday'],
                    'sort': 'asc',
                    'chainid': '1'
                }
            },
            {
                'name': 'stats_dailynewaddress',
                'params': {
                    'module': 'stats',
                    'action': 'dailynewaddress',
                    'startdate': self.test_data['week_ago'],
                    'enddate': self.test_data['yesterday'],
                    'sort': 'asc',
                    'chainid': '1'
                }
            },
            {
                'name': 'stats_dailynetutilization',
                'params': {
                    'module': 'stats',
                    'action': 'dailynetutilization',
                    'startdate': self.test_data['week_ago'],
                    'enddate': self.test_data['yesterday'],
                    'sort': 'asc',
                    'chainid': '1'
                }
            },
            {
                'name': 'stats_dailyavghashrate',
                'params': {
                    'module': 'stats',
                    'action': 'dailyavghashrate',
                    'startdate': self.test_data['week_ago'],
                    'enddate': self.test_data['yesterday'],
                    'sort': 'asc',
                    'chainid': '1'
                }
            },
            {
                'name': 'stats_dailytx',
                'params': {
                    'module': 'stats',
                    'action': 'dailytx',
                    'startdate': self.test_data['week_ago'],
                    'enddate': self.test_data['yesterday'],
                    'sort': 'asc',
                    'chainid': '1'
                }
            },
            {
                'name': 'stats_dailyavgnetdifficulty',
                'params': {
                    'module': 'stats',
                    'action': 'dailyavgnetdifficulty',
                    'startdate': self.test_data['week_ago'],
                    'enddate': self.test_data['yesterday'],
                    'sort': 'asc',
                    'chainid': '1'
                }
            },
            {
                'name': 'stats_ethdailyprice',
                'params': {
                    'module': 'stats',
                    'action': 'ethdailyprice',
                    'startdate': self.test_data['week_ago'],
                    'enddate': self.test_data['yesterday'],
                    'sort': 'asc',
                    'chainid': '1'
                }
            }
        ]
        
        for test in stats_tests:
            self._run_single_test('Statistics', test)

    def _test_logs_tools(self):
        """Test logs-related tools."""
        print("\n📝 Testing Logs Tools...")
        
        logs_tests = [
            {
                'name': 'logs_getLogsByAddress',
                'params': {
                    'module': 'logs',
                    'action': 'getLogs',
                    'address': self.test_data['usdt_contract'],
                    'fromBlock': self.test_data['older_block'],
                    'toBlock': self.test_data['recent_block'],
                    'page': '1',
                    'offset': '10',
                    'chainid': '1'
                }
            },
            {
                'name': 'logs_getLogsByTopics',
                'params': {
                    'module': 'logs',
                    'action': 'getLogs',
                    'fromBlock': self.test_data['older_block'],
                    'toBlock': self.test_data['recent_block'],
                    'topic0': '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef',  # Transfer event
                    'page': '1',
                    'offset': '10',
                    'chainid': '1'
                }
            },
            {
                'name': 'logs_getLogsByAddressAndTopics',
                'params': {
                    'module': 'logs',
                    'action': 'getLogs',
                    'address': self.test_data['usdt_contract'],
                    'fromBlock': self.test_data['older_block'],
                    'toBlock': self.test_data['recent_block'],
                    'topic0': '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef',  # Transfer event
                    'page': '1',
                    'offset': '10',
                    'chainid': '1'
                }
            }
        ]
        
        for test in logs_tests:
            self._run_single_test('Logs', test)

    def _test_rpc_tools(self):
        """Test RPC proxy tools."""
        print("\n🔗 Testing RPC Tools...")
        
        rpc_tests = [
            {
                'name': 'proxy_eth_blockNumber',
                'params': {
                    'module': 'proxy',
                    'action': 'eth_blockNumber',
                    'chainid': '1'
                }
            },
            {
                'name': 'proxy_eth_gasPrice',
                'params': {
                    'module': 'proxy',
                    'action': 'eth_gasPrice',
                    'chainid': '1'
                }
            },
            {
                'name': 'proxy_eth_getTransactionByHash',
                'params': {
                    'module': 'proxy',
                    'action': 'eth_getTransactionByHash',
                    'txhash': self.test_data['known_tx'],
                    'chainid': '1'
                }
            },
            {
                'name': 'proxy_eth_getBlockByNumber',
                'params': {
                    'module': 'proxy',
                    'action': 'eth_getBlockByNumber',
                    'tag': hex(int(self.test_data['recent_block'])),
                    'boolean': 'true',
                    'chainid': '1'
                }
            },
            {
                'name': 'proxy_eth_getTransactionCount',
                'params': {
                    'module': 'proxy',
                    'action': 'eth_getTransactionCount',
                    'address': self.test_data['vitalik_address'],
                    'tag': 'latest',
                    'chainid': '1'
                }
            },
            {
                'name': 'proxy_eth_getUncleByBlockNumberAndIndex',
                'params': {
                    'module': 'proxy',
                    'action': 'eth_getUncleByBlockNumberAndIndex',
                    'tag': self.test_data['recent_block'],
                    'index': '0x0',
                    'chainid': '1'
                }
            },
            {
                'name': 'proxy_eth_getBlockTransactionCountByNumber',
                'params': {
                    'module': 'proxy',
                    'action': 'eth_getBlockTransactionCountByNumber',
                    'tag': self.test_data['recent_block'],
                    'chainid': '1'
                }
            },
            {
                'name': 'proxy_eth_getTransactionByBlockNumberAndIndex',
                'params': {
                    'module': 'proxy',
                    'action': 'eth_getTransactionByBlockNumberAndIndex',
                    'tag': self.test_data['recent_block'],
                    'index': '0x0',
                    'chainid': '1'
                }
            },
            {
                'name': 'proxy_eth_getTransactionReceipt',
                'params': {
                    'module': 'proxy',
                    'action': 'eth_getTransactionReceipt',
                    'txhash': self.test_data['known_tx'],
                    'chainid': '1'
                }
            },
            {
                'name': 'proxy_eth_call',
                'params': {
                    'module': 'proxy',
                    'action': 'eth_call',
                    'to': self.test_data['usdt_contract'],
                    'data': '0x18160ddd',  # totalSupply() function signature
                    'tag': 'latest',
                    'chainid': '1'
                }
            },
            {
                'name': 'proxy_eth_getCode',
                'params': {
                    'module': 'proxy',
                    'action': 'eth_getCode',
                    'address': self.test_data['usdt_contract'],
                    'tag': 'latest',
                    'chainid': '1'
                }
            },
            {
                'name': 'proxy_eth_getStorageAt',
                'params': {
                    'module': 'proxy',
                    'action': 'eth_getStorageAt',
                    'address': self.test_data['usdt_contract'],
                    'position': '0x0',
                    'tag': 'latest',
                    'chainid': '1'
                }
            },
            {
                'name': 'proxy_eth_estimateGas',
                'params': {
                    'module': 'proxy',
                    'action': 'eth_estimateGas',
                    'data': '0xa9059cbb000000000000000000000000d8da6bf26964af9d7eed9e03e53415d37aa96045000000000000000000000000000000000000000000000000000000000000000a',
                    'to': self.test_data['usdt_contract'],
                    'value': '0x0',
                    'gasPrice': '0x9184e72a000',
                    'gas': '0x76c0',
                    'chainid': '1'
                }
            }
        ]
        
        for test in rpc_tests:
            self._run_single_test('RPC', test)

    def _run_single_test(self, category, test_config):
        """Run a single test and record results."""
        tool_name = test_config['name']
        params = test_config['params']
        
        print(f"  Testing {tool_name}...")
        
        # Make actual API call
        result = self.test_tool(tool_name, params)
        
        if category not in self.results:
            self.results[category] = {}
            
        self.results[category][tool_name] = {
            'test_params': params,
            'result': result,
            'recommendation': self._categorize_tool(result)
        }
        
        # Print quick result
        status = "✅" if result['success'] else "❌"
        print(f"    {status} {tool_name} - {result.get('output_length', 0)} chars, {result.get('response_time', 0)}s")

    def _categorize_tool(self, result):
        """Categorize tool based on test results."""
        if not result['success']:
            if result['requires_pro']:
                return '🔴 Not Recommended - Requires Pro Account'
            else:
                return '🔴 Not Recommended - API Error'
        
        if result['output_length'] > 10000:
            return '🔴 Not Recommended - Output Too Large'
        elif result['output_length'] > 5000:
            return '🟡 Situational - Large Output'
        elif result['response_time'] > 5.0:
            return '🟡 Situational - Slow Response'
        else:
            return '🟢 Essential - Good for Agents'

    def generate_report(self):
        """Generate a comprehensive report of all test results."""
        report = {
            'timestamp': datetime.now().isoformat(),
            'total_tools_tested': sum(len(category) for category in self.results.values()),
            'summary': {},
            'detailed_results': self.results,
            'recommendations': {
                'essential': [],
                'situational': [],
                'not_recommended': []
            }
        }
        
        # Categorize all tools
        for category, tools in self.results.items():
            for tool_name, tool_data in tools.items():
                recommendation = tool_data['recommendation']
                tool_info = {
                    'name': tool_name,
                    'category': category,
                    'output_length': tool_data['result']['output_length'],
                    'response_time': tool_data['result']['response_time']
                }
                
                if '🟢' in recommendation:
                    report['recommendations']['essential'].append(tool_info)
                elif '🟡' in recommendation:
                    report['recommendations']['situational'].append(tool_info)
                else:
                    report['recommendations']['not_recommended'].append(tool_info)
        
        # Generate summary
        report['summary'] = {
            'essential_count': len(report['recommendations']['essential']),
            'situational_count': len(report['recommendations']['situational']),
            'not_recommended_count': len(report['recommendations']['not_recommended'])
        }
        
        return report

def main():
    """Main function to run all tests."""
    print("🚀 Etherscan MCP Tool Testing Suite")
    print("=" * 50)
    
    tester = ToolTester()
    
    # Run all tests
    results = tester.run_all_tests()
    
    # Generate report
    report = tester.generate_report()
    
    # Save results to file
    with open('tool_test_results.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    # Print summary
    print("\n" + "=" * 80)
    print("📊 TEST SUMMARY")
    print("=" * 80)
    print(f"Total Tools Tested: {report['total_tools_tested']}")
    print(f"🟢 Essential Tools: {report['summary']['essential_count']}")
    print(f"🟡 Situational Tools: {report['summary']['situational_count']}")
    print(f"🔴 Not Recommended: {report['summary']['not_recommended_count']}")
    
    print(f"\n📁 Detailed results saved to: tool_test_results.json")
    
    return report

if __name__ == "__main__":
    main()