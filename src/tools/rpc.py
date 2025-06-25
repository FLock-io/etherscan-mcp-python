"""RPC (proxy) tools for Etherscan API."""

from typing import Optional
from mcp.server.fastmcp import FastMCP
from .utils import api_call


def register_rpc_tools(server: FastMCP) -> None:
    """Register all RPC proxy tools with the server."""
    
    @server.tool()
    def proxy_eth_blockNumber(chainid: str = "1") -> str:
        """Returns the number of most recent block.
        
        Args:
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "proxy",
            "action": "eth_blockNumber",
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def proxy_eth_getBlockByNumber(tag: str, boolean: bool, chainid: str = "1") -> str:
        """Returns information about a block by block number.
        
        Args:
            tag: The block number, in hex eg. 0xC36B3C
            boolean: When true, returns full transaction objects and their information, when false only returns a list of transactions
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "proxy",
            "action": "eth_getBlockByNumber",
            "tag": tag,
            "boolean": str(boolean).lower(),
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def proxy_eth_getUncleByBlockNumberAndIndex(tag: str, index: str, chainid: str = "1") -> str:
        """Returns information about a uncle by block number.
        
        Args:
            tag: The block number, in hex eg. 0xC36B3C
            index: The position of the uncle's index in the block, in hex eg. 0x5
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "proxy",
            "action": "eth_getUncleByBlockNumberAndIndex",
            "tag": tag,
            "index": index,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def proxy_eth_getBlockTransactionCountByNumber(tag: str, chainid: str = "1") -> str:
        """Returns the number of transactions in a block.
        
        Args:
            tag: The block number, in hex eg. 0xC36B3C
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "proxy",
            "action": "eth_getBlockTransactionCountByNumber",
            "tag": tag,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def proxy_eth_getTransactionByHash(txhash: str, chainid: str = "1") -> str:
        """Returns information about a transaction requested by transaction hash.
        
        Args:
            txhash: The string representing the hash of the transaction
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "proxy",
            "action": "eth_getTransactionByHash",
            "txhash": txhash,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def proxy_eth_getTransactionByBlockNumberAndIndex(tag: str, index: str, chainid: str = "1") -> str:
        """Returns information about a transaction requested by block number and transaction index position.
        
        Args:
            tag: The block number, in hex eg. 0xC36B3C
            index: The position of the uncle's index in the block, in hex eg. 0x5
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "proxy",
            "action": "eth_getTransactionByBlockNumberAndIndex",
            "tag": tag,
            "index": index,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def proxy_eth_getTransactionCount(address: str, tag: str, chainid: str = "1") -> str:
        """Returns the number of transactions performed by an address.
        
        Args:
            address: The string representing the address to get transaction count
            tag: The string pre-defined block parameter, either `earliest`, `pending` or `latest`
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "proxy",
            "action": "eth_getTransactionCount",
            "address": address,
            "tag": tag,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def proxy_eth_getTransactionReceipt(txhash: str, chainid: str = "1") -> str:
        """Returns the receipt of a transaction that has been validated.
        
        Args:
            txhash: The string representing the hash of the transaction
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "proxy",
            "action": "eth_getTransactionReceipt",
            "txhash": txhash,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def proxy_eth_call(to: str, data: str, tag: str, chainid: str = "1") -> str:
        """Executes a new message call immediately without creating a transaction on the block chain.
        
        Args:
            to: The string representing the address to interact with
            data: The hash of the method signature and encoded parameters
            tag: The string pre-defined block parameter, either `earliest`, `pending` or `latest`
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "proxy",
            "action": "eth_call",
            "to": to,
            "data": data,
            "tag": tag,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def proxy_eth_getCode(address: str, tag: str, chainid: str = "1") -> str:
        """Returns code at a given address.
        
        Args:
            address: The string representing the address to get code
            tag: The string pre-defined block parameter, either `earliest`, `pending` or `latest`
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "proxy",
            "action": "eth_getCode",
            "address": address,
            "tag": tag,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def proxy_eth_getStorageAt(address: str, position: str, tag: str, chainid: str = "1") -> str:
        """Returns the value from a storage position at a given address.
        
        Args:
            address: The string representing the address to get code
            position: The hex code of the position in storage, eg 0x0
            tag: The string pre-defined block parameter, either `earliest`, `pending` or `latest`
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "proxy",
            "action": "eth_getStorageAt",
            "address": address,
            "position": position,
            "tag": tag,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def proxy_eth_gasPrice(chainid: str = "1") -> str:
        """Returns the current price per gas in wei.
        
        Args:
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "proxy",
            "action": "eth_gasPrice",
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def proxy_eth_estimateGas(
        data: str,
        to: str,
        value: Optional[str] = None,
        gas: Optional[str] = None,
        gasPrice: Optional[str] = None,
        chainid: str = "1"
    ) -> str:
        """Makes a call or transaction, which won't be added to the blockchain and returns the used gas.
        
        Args:
            data: The hash of the method signature and encoded parameters
            to: The string representing the address to interact with
            value: The value sent in this transaction, in hex eg. 0xff22
            gas: The amount of gas provided for the transaction, in hex eg. 0x5f5e0ff
            gasPrice: The gas price paid for each unit of gas, in wei
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "proxy",
            "action": "eth_estimateGas",
            "data": data,
            "to": to,
            "chainid": chainid
        }
        
        # Add optional parameters if provided
        if value is not None:
            params["value"] = value
        if gas is not None:
            params["gas"] = gas
        if gasPrice is not None:
            params["gasPrice"] = gasPrice
            
        return api_call(params)