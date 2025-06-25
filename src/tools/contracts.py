"""Contract-related tools for Etherscan API."""

from mcp.server.fastmcp import FastMCP
from .utils import api_call


def register_contract_tools(server: FastMCP) -> None:
    """Register all contract-related tools with the server."""
    
    @server.tool()
    def contract_getabi(address: str, chainid: str = "1") -> str:
        """Returns the Contract Application Binary Interface (ABI) of a verified smart contract.
        
        Args:
            address: The contract address that has a verified source code
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "contract",
            "action": "getabi",
            "address": address,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def contract_getsourcecode(address: str, chainid: str = "1") -> str:
        """Returns the Contract Source Code for Verified Contract Source Codes.
        
        Args:
            address: The contract address that has a verified source code
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "contract",
            "action": "getsourcecode",
            "address": address,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def contract_getcontractcreation(contractaddresses: str, chainid: str = "1") -> str:
        """Returns the Contract Creator and Creation Tx Hash.
        
        Args:
            contractaddresses: The contract address to check for contract creator and creation tx hash, up to 5 at a time
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "contract",
            "action": "getcontractcreation",
            "contractaddresses": contractaddresses,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def contract_checkverifystatus(guid: str, chainid: str = "1") -> str:
        """Returns the success or error status of a contract verification request.
        
        Args:
            guid: The unique guid received from the verification request
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "contract",
            "action": "checkverifystatus",
            "guid": guid,
            "chainid": chainid
        }
        return api_call(params)