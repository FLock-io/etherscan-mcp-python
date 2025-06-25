"""Account-related tools for Etherscan API."""

from typing import Optional
from mcp.server.fastmcp import FastMCP
from .utils import api_call


def register_account_tools(server: FastMCP) -> None:
    """Register all account-related tools with the server."""
    
    @server.tool()
    def account_balance(address: str, chainid: str = "1") -> str:
        """Returns the Ether balance of a given address.
        
        Args:
            address: The string representing the address to check for balance
            chainid: The chain id, default is 1
        """
        params = {
            "module": "account",
            "action": "balance",
            "address": address,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def account_balancemulti(address: str, chainid: str = "1") -> str:
        """Get Ether Balance for Multiple Addresses in a Single Call.
        
        Args:
            address: The strings representing the addresses to check for balance, separated by `,`
                    up to **20 addresses** per call
            chainid: The chain id, default is 1
        """
        params = {
            "module": "account",
            "action": "balancemulti",
            "address": address,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def account_txlist(
        address: str,
        startblock: str = "0",
        endblock: str = "99999999",
        page: str = "1",
        offset: str = "10",
        sort: str = "asc",
        chainid: str = "1"
    ) -> str:
        """Returns the list of 'Normal' Transactions By Address.
        
        Args:
            address: The string representing the address to check for transactions
            startblock: The integer block number to start searching for transactions
            endblock: The integer block number to stop searching for transactions
            page: The integer page number, if pagination is enabled
            offset: The number of transactions displayed per page
            sort: The sorting preference, use `asc` to sort by ascending and `desc` to sort by descending
            chainid: The chain id, default is 1
        """
        params = {
            "module": "account",
            "action": "txlist",
            "address": address,
            "startblock": startblock,
            "endblock": endblock,
            "page": page,
            "offset": offset,
            "sort": sort,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def account_txlistinternal(
        address: str,
        startblock: str = "0",
        endblock: str = "99999999",
        page: str = "1",
        offset: str = "10",
        sort: str = "asc",
        chainid: str = "1"
    ) -> str:
        """Returns the list of 'Internal' Transactions by Address.
        
        Args:
            address: The string representing the address to get internal txs for
            startblock: The integer block number to start searching for transactions
            endblock: The integer block number to stop searching for transactions
            page: The integer page number, if pagination is enabled
            offset: The number of transactions displayed per page
            sort: The sorting preference, use `asc` to sort by ascending and `desc` to sort by descending
            chainid: The chain id, default is 1
        """
        params = {
            "module": "account",
            "action": "txlistinternal",
            "address": address,
            "startblock": startblock,
            "endblock": endblock,
            "page": page,
            "offset": offset,
            "sort": sort,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def account_txlistinternal_byhash(txhash: str, chainid: str = "1") -> str:
        """Returns the list of 'Internal' Transactions by Transaction Hash.
        
        Args:
            txhash: The string representing the transaction hash to get internal txs for
            chainid: The chain id, default is 1
        """
        params = {
            "module": "account",
            "action": "txlistinternal",
            "txhash": txhash,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def account_txlistinternal_byblock(
        startblock: str,
        endblock: str,
        page: str = "1",
        offset: str = "10",
        sort: str = "asc",
        chainid: str = "1"
    ) -> str:
        """Returns the list of 'Internal' Transactions by Block Range.
        
        Args:
            startblock: The integer block number to start searching for transactions
            endblock: The integer block number to stop searching for transactions
            page: The integer page number, if pagination is enabled
            offset: The number of transactions displayed per page
            sort: The sorting preference, use `asc` to sort by ascending and `desc` to sort by descending
            chainid: The chain id, default is 1
        """
        params = {
            "module": "account",
            "action": "txlistinternal",
            "startblock": startblock,
            "endblock": endblock,
            "page": page,
            "offset": offset,
            "sort": sort,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def account_tokentx(
        address: str,
        contractaddress: Optional[str] = None,
        startblock: str = "0",
        endblock: str = "99999999",
        page: str = "1",
        offset: str = "10",
        sort: str = "asc",
        chainid: str = "1"
    ) -> str:
        """Returns the list of ERC20 Token Transfer Events by Address.
        
        Args:
            address: The string representing the address to get token transfers for
            contractaddress: The string representing the token contract address to check for balance
            startblock: The integer block number to start searching for transactions
            endblock: The integer block number to stop searching for transactions
            page: The integer page number, if pagination is enabled
            offset: The number of transactions displayed per page
            sort: The sorting preference, use `asc` to sort by ascending and `desc` to sort by descending
            chainid: The chain id, default is 1
        """
        params = {
            "module": "account",
            "action": "tokentx",
            "address": address,
            "startblock": startblock,
            "endblock": endblock,
            "page": page,
            "offset": offset,
            "sort": sort,
            "chainid": chainid
        }
        if contractaddress:
            params["contractaddress"] = contractaddress
        return api_call(params)
    
    @server.tool()
    def account_tokennfttx(
        address: str,
        contractaddress: Optional[str] = None,
        startblock: str = "0",
        endblock: str = "99999999",
        page: str = "1",
        offset: str = "10",
        sort: str = "asc",
        chainid: str = "1"
    ) -> str:
        """Returns the list of ERC721 Token Transfer Events by Address.
        
        Args:
            address: The string representing the address to get NFT transfers for
            contractaddress: The string representing the NFT contract address to check for balance
            startblock: The integer block number to start searching for transactions
            endblock: The integer block number to stop searching for transactions
            page: The integer page number, if pagination is enabled
            offset: The number of transactions displayed per page
            sort: The sorting preference, use `asc` to sort by ascending and `desc` to sort by descending
            chainid: The chain id, default is 1
        """
        params = {
            "module": "account",
            "action": "tokennfttx",
            "address": address,
            "startblock": startblock,
            "endblock": endblock,
            "page": page,
            "offset": offset,
            "sort": sort,
            "chainid": chainid
        }
        if contractaddress:
            params["contractaddress"] = contractaddress
        return api_call(params)
    
    @server.tool()
    def account_token1155tx(
        address: str,
        contractaddress: Optional[str] = None,
        startblock: str = "0",
        endblock: str = "99999999",
        page: str = "1",
        offset: str = "10",
        sort: str = "asc",
        chainid: str = "1"
    ) -> str:
        """Returns the list of ERC1155 Token Transfer Events by Address.
        
        Args:
            address: The string representing the address to get ERC1155 transfers for
            contractaddress: The string representing the ERC1155 contract address to check for balance
            startblock: The integer block number to start searching for transactions
            endblock: The integer block number to stop searching for transactions
            page: The integer page number, if pagination is enabled
            offset: The number of transactions displayed per page
            sort: The sorting preference, use `asc` to sort by ascending and `desc` to sort by descending
            chainid: The chain id, default is 1
        """
        params = {
            "module": "account",
            "action": "token1155tx",
            "address": address,
            "startblock": startblock,
            "endblock": endblock,
            "page": page,
            "offset": offset,
            "sort": sort,
            "chainid": chainid
        }
        if contractaddress:
            params["contractaddress"] = contractaddress
        return api_call(params)
    
    @server.tool()
    def account_fundedby(address: str, chainid: str = "1") -> str:
        """Returns the address that funded an address, and its relative age.
        
        Args:
            address: The string representing the address that received funding
            chainid: The chain id, default is 1
        """
        params = {
            "module": "account",
            "action": "fundedby",
            "address": address,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def account_getminedblocks(
        address: str,
        blocktype: str = "blocks",
        page: str = "1",
        offset: str = "10",
        chainid: str = "1"
    ) -> str:
        """Returns the list of blocks validated by an address.
        
        Args:
            address: The string representing the address to check for validated blocks
            blocktype: The string pre-defined block type, either `blocks` for canonical blocks or `uncles` for uncle blocks only
            page: The integer page number, if pagination is enabled
            offset: The number of blocks displayed per page
            chainid: The chain id, default is 1
        """
        params = {
            "module": "account",
            "action": "getminedblocks",
            "address": address,
            "blocktype": blocktype,
            "page": page,
            "offset": offset,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def account_txsBeaconWithdrawal(
        address: str,
        startblock: str = "0",
        endblock: str = "99999999",
        page: str = "1",
        offset: str = "100",
        sort: str = "asc",
        chainid: str = "1"
    ) -> str:
        """Returns the beacon chain withdrawals made to an address.
        
        Args:
            address: The string representing the address to check for beacon withdrawals
            startblock: The integer block number to start searching for transactions
            endblock: The integer block number to stop searching for transactions
            page: The integer page number, if pagination is enabled
            offset: The number of withdrawals displayed per page
            sort: The sorting preference, use `asc` to sort by ascending and `desc` to sort by descending
            chainid: The chain id, default is 1
        """
        params = {
            "module": "account",
            "action": "txsBeaconWithdrawal",
            "address": address,
            "startblock": startblock,
            "endblock": endblock,
            "page": page,
            "offset": offset,
            "sort": sort,
            "chainid": chainid
        }
        return api_call(params)