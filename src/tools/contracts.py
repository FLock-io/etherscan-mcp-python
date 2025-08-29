"""Contract-related tools for Etherscan API."""

from mcp.server.fastmcp import FastMCP
from .utils import api_call, api_call_filtered


def register_contract_tools(server: FastMCP) -> None:
    """Register all contract-related tools with the server."""
    
    @server.tool()
    def contract_getabi(address: str, chainid: str = "1") -> str:
        """Returns the Contract Application Binary Interface (ABI) of a verified smart contract.
        Note: This provides the full ABI for contract interaction. For agents needing 
        lighter metadata, use contract_getsourcecode which excludes the full ABI.
        
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
        # Keep ABI as-is for agents that need contract interaction capabilities
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
        # Remove massive source code and ABI fields for agents (keep metadata only)
        fields_to_remove = {"SourceCode", "ABI"}
        return api_call_filtered(params, fields_to_remove)
    
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
        # Remove massive bytecode field that's not useful for agents (99% size reduction)
        fields_to_remove = {"creationBytecode"}
        return api_call_filtered(params, fields_to_remove)
    
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