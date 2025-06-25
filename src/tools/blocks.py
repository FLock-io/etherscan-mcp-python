"""Block-related tools for Etherscan API."""

from mcp.server.fastmcp import FastMCP
from .utils import api_call


def register_block_tools(server: FastMCP) -> None:
    """Register all block-related tools with the server."""
    
    @server.tool()
    def block_getblockreward(blockno: str, chainid: str = "1") -> str:
        """Returns the block reward and 'Uncle' block rewards.
        
        Args:
            blockno: The integer block number to check block rewards for
            chainid: The chain id, default is 1
        """
        params = {
            "module": "block",
            "action": "getblockreward",
            "blockno": blockno,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def block_getblockcountdown(blockno: str, chainid: str = "1") -> str:
        """Returns the estimated time remaining, in seconds, until a certain block is mined.
        
        Args:
            blockno: The integer block number to estimate time remaining to be mined
            chainid: The chain id, default is 1
        """
        params = {
            "module": "block",
            "action": "getblockcountdown",
            "blockno": blockno,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def block_getblocknobytime(timestamp: str, closest: str, chainid: str = "1") -> str:
        """Returns the block number that was mined at a certain timestamp.
        
        Args:
            timestamp: The integer representing the Unix timestamp in **seconds**
            closest: The closest available block to the provided timestamp, either `before` or `after`
            chainid: The chain id, default is 1
        """
        params = {
            "module": "block",
            "action": "getblocknobytime",
            "timestamp": timestamp,
            "closest": closest,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def block_getblocktxnscount(blockno: str, chainid: str = "1") -> str:
        """Returns the number of transactions in a specified block.
        
        Args:
            blockno: The integer block number to get the transaction count for
            chainid: The chain id, default is 1
        """
        params = {
            "module": "block",
            "action": "getblocktxnscount",
            "blockno": blockno,
            "chainid": chainid
        }
        return api_call(params)