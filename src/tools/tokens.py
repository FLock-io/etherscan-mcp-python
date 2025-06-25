"""Token-related tools for Etherscan API."""

from mcp.server.fastmcp import FastMCP
from .utils import api_call


def register_token_tools(server: FastMCP) -> None:
    """Register all token-related tools with the server."""
    
    @server.tool()
    def stats_tokensupply(contractaddress: str, chainid: str = "1") -> str:
        """Returns the current amount of an ERC-20 token in circulation.
        
        Args:
            contractaddress: The contract address of the ERC-20 token
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "stats",
            "action": "tokensupply",
            "contractaddress": contractaddress,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def account_tokenbalance(contractaddress: str, address: str, chainid: str = "1") -> str:
        """Returns the current balance of an ERC-20 token of an address.
        
        Args:
            contractaddress: The contract address of the ERC-20 token
            address: The string representing the address to check for token balance
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "account",
            "action": "tokenbalance",
            "contractaddress": contractaddress,
            "address": address,
            "tag": "latest",
            "chainid": chainid
        }
        return api_call(params)