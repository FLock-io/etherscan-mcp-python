"""Logs-related tools for Etherscan API."""

from typing import Optional
from mcp.server.fastmcp import FastMCP
from .utils import api_call


def register_logs_tools(server: FastMCP) -> None:
    """Register all logs-related tools with the server."""
    
    @server.tool()
    def logs_getLogsByAddress(
        address: str,
        fromBlock: Optional[str] = None,
        toBlock: Optional[str] = None,
        page: str = "1",
        offset: str = "1000",
        chainid: str = "1"
    ) -> str:
        """Returns the event logs from an address, with optional filtering by block range.
        
        Args:
            address: The string representing the address to check for logs
            fromBlock: The integer block number to start searching for logs eg. 12878196
            toBlock: The integer block number to stop searching for logs eg. 12879196
            page: The integer page number, if pagination is enabled
            offset: The number of transactions displayed per page limited to **1000 records** per query
            chainid: The chain id, default is 1
        """
        params = {
            "module": "logs",
            "action": "getLogs",
            "address": address,
            "page": page,
            "offset": offset,
            "chainid": chainid
        }
        if fromBlock:
            params["fromBlock"] = fromBlock
        if toBlock:
            params["toBlock"] = toBlock
        return api_call(params)
    
    @server.tool()
    def logs_getLogsByTopics(
        fromBlock: str,
        toBlock: str,
        topic0: Optional[str] = None,
        topic1: Optional[str] = None,
        topic2: Optional[str] = None,
        topic3: Optional[str] = None,
        topic0_1_opr: Optional[str] = None,
        topic1_2_opr: Optional[str] = None,
        topic2_3_opr: Optional[str] = None,
        topic0_2_opr: Optional[str] = None,
        topic0_3_opr: Optional[str] = None,
        topic1_3_opr: Optional[str] = None,
        page: Optional[str] = None,
        offset: Optional[str] = None,
        chainid: str = "1"
    ) -> str:
        """Returns the events log in a block range, filtered by topics.
        
        Args:
            fromBlock: The integer block number to start searching for logs eg. 12878196
            toBlock: The integer block number to stop searching for logs eg. 12879196
            topic0: The topic numbers to search for limited to topic0, topic1, topic2, topic3
            topic1: The topic numbers to search for limited to topic0, topic1, topic2, topic3
            topic2: The topic numbers to search for limited to topic0, topic1, topic2, topic3
            topic3: The topic numbers to search for limited to topic0, topic1, topic2, topic3
            topic0_1_opr: The topic operator when multiple topic combinations are used limited to `and` or `or`
            topic1_2_opr: The topic operator when multiple topic combinations are used limited to `and` or `or`
            topic2_3_opr: The topic operator when multiple topic combinations are used limited to `and` or `or`
            topic0_2_opr: The topic operator when multiple topic combinations are used limited to `and` or `or`
            topic0_3_opr: The topic operator when multiple topic combinations are used limited to `and` or `or`
            topic1_3_opr: The topic operator when multiple topic combinations are used limited to `and` or `or`
            page: The integer page number, if pagination is enabled
            offset: The number of transactions displayed per page limited to **1000 records** per query
            chainid: The chain id, default is 1
        """
        params = {
            "module": "logs",
            "action": "getLogs",
            "fromBlock": fromBlock,
            "toBlock": toBlock,
            "chainid": chainid
        }
        
        # Add optional parameters if provided
        optional_params = {
            "topic0": topic0,
            "topic1": topic1,
            "topic2": topic2,
            "topic3": topic3,
            "topic0_1_opr": topic0_1_opr,
            "topic1_2_opr": topic1_2_opr,
            "topic2_3_opr": topic2_3_opr,
            "topic0_2_opr": topic0_2_opr,
            "topic0_3_opr": topic0_3_opr,
            "topic1_3_opr": topic1_3_opr,
            "page": page,
            "offset": offset
        }
        
        for key, value in optional_params.items():
            if value is not None:
                params[key] = value
                
        return api_call(params)
    
    @server.tool()
    def logs_getLogsByAddressAndTopics(
        fromBlock: str,
        toBlock: str,
        address: str,
        topic0: Optional[str] = None,
        topic1: Optional[str] = None,
        topic2: Optional[str] = None,
        topic3: Optional[str] = None,
        topic0_1_opr: Optional[str] = None,
        topic1_2_opr: Optional[str] = None,
        topic2_3_opr: Optional[str] = None,
        topic0_2_opr: Optional[str] = None,
        topic0_3_opr: Optional[str] = None,
        topic1_3_opr: Optional[str] = None,
        page: Optional[str] = None,
        offset: Optional[str] = None,
        chainid: str = "1"
    ) -> str:
        """Returns the event logs from an address, filtered by topics and block range.
        
        Args:
            fromBlock: The integer block number to start searching for logs eg. 12878196
            toBlock: The integer block number to stop searching for logs eg. 12879196
            address: The string representing the address to check for logs
            topic0: The topic numbers to search for limited to topic0, topic1, topic2, topic3
            topic1: The topic numbers to search for limited to topic0, topic1, topic2, topic3
            topic2: The topic numbers to search for limited to topic0, topic1, topic2, topic3
            topic3: The topic numbers to search for limited to topic0, topic1, topic2, topic3
            topic0_1_opr: The topic operator when multiple topic combinations are used limited to `and` or `or`
            topic1_2_opr: The topic operator when multiple topic combinations are used limited to `and` or `or`
            topic2_3_opr: The topic operator when multiple topic combinations are used limited to `and` or `or`
            topic0_2_opr: The topic operator when multiple topic combinations are used limited to `and` or `or`
            topic0_3_opr: The topic operator when multiple topic combinations are used limited to `and` or `or`
            topic1_3_opr: The topic operator when multiple topic combinations are used limited to `and` or `or`
            page: The integer page number, if pagination is enabled
            offset: The number of transactions displayed per page limited to **1000 records** per query
            chainid: The chain id, default is 1
        """
        params = {
            "module": "logs",
            "action": "getLogs",
            "fromBlock": fromBlock,
            "toBlock": toBlock,
            "address": address,
            "chainid": chainid
        }
        
        # Add optional parameters if provided
        optional_params = {
            "topic0": topic0,
            "topic1": topic1,
            "topic2": topic2,
            "topic3": topic3,
            "topic0_1_opr": topic0_1_opr,
            "topic1_2_opr": topic1_2_opr,
            "topic2_3_opr": topic2_3_opr,
            "topic0_2_opr": topic0_2_opr,
            "topic0_3_opr": topic0_3_opr,
            "topic1_3_opr": topic1_3_opr,
            "page": page,
            "offset": offset
        }
        
        for key, value in optional_params.items():
            if value is not None:
                params[key] = value
                
        return api_call(params)