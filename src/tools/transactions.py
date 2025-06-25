"""Transaction-related tools for Etherscan API."""

from mcp.server.fastmcp import FastMCP
from .utils import api_call


def register_transaction_tools(server: FastMCP) -> None:
    """Register all transaction-related tools with the server."""
    
    @server.tool()
    def transaction_getstatus(txhash: str, chainid: str = "1") -> str:
        """Returns the status code of a contract execution.
        
        Args:
            txhash: The string representing the transaction hash to check the execution status
            chainid: The chain id, default is 1
        """
        params = {
            "module": "transaction",
            "action": "getstatus",
            "txhash": txhash,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def transaction_gettxreceiptstatus(txhash: str, chainid: str = "1") -> str:
        """Returns the status code of a transaction execution.
        
        Args:
            txhash: The string representing the transaction hash to check the execution status
            chainid: The chain id, default is 1
        """
        params = {
            "module": "transaction",
            "action": "gettxreceiptstatus",
            "txhash": txhash,
            "chainid": chainid
        }
        return api_call(params)