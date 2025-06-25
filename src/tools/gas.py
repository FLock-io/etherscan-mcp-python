"""Gas-related tools for Etherscan API."""

from mcp.server.fastmcp import FastMCP
from .utils import api_call


def register_gas_tools(server: FastMCP) -> None:
    """Register all gas-related tools with the server."""
    
    @server.tool()
    def gas_gasestimate(gasprice: str, chainid: str = "1") -> str:
        """Returns the estimated time, in seconds, for a transaction to be confirmed on the blockchain.
        
        Args:
            gasprice: The price paid per unit of gas, in wei
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "gastracker",
            "action": "gasestimate",
            "gasprice": gasprice,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def gas_gasoracle(chainid: str = "1") -> str:
        """Returns the current Safe, Proposed and Fast gas prices.
        
        Args:
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "gastracker",
            "action": "gasoracle",
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def stats_dailyavggaslimit(startdate: str, enddate: str, sort: str, chainid: str = "1") -> str:
        """Returns the historical daily average gas limit of the Ethereum network.
        
        Args:
            startdate: The starting date in yyyy-MM-dd format, eg. 2019-01-31
            enddate: The ending date in yyyy-MM-dd format, eg. 2019-02-28
            sort: The sorting preference, use `asc` to sort by ascending and `desc` to sort by descending
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "stats",
            "action": "dailyavggaslimit",
            "startdate": startdate,
            "enddate": enddate,
            "sort": sort,
            "chainid": chainid
        }
        return api_call(params)