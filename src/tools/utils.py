"""Utility functions for Etherscan API interactions."""

import os
import httpx
from typing import Any, Dict, Optional
from mcp.server.fastmcp import FastMCP


class EtherscanAPIError(Exception):
    """Exception raised for Etherscan API errors."""
    pass


async def make_api_request(params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Make an API request to Etherscan.
    
    Args:
        params: Dictionary of API parameters
        
    Returns:
        JSON response from Etherscan API
        
    Raises:
        EtherscanAPIError: If API request fails or returns error
    """
    api_key = os.getenv("ETHERSCAN_API_KEY")
    if not api_key:
        raise EtherscanAPIError("ETHERSCAN_API_KEY environment variable is not set")
    
    # Build query parameters
    query_params = {}
    for key, value in params.items():
        if value is not None:
            query_params[key] = str(value)
    
    query_params["apikey"] = api_key
    
    url = "https://api.etherscan.io/v2/api"
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, params=query_params)
            response.raise_for_status()
            
            data = response.json()
            
            # Check if API returned an error
            if data.get("status") == "0" and data.get("message") != "No transactions found":
                error_msg = data.get("result", data.get("message", "Unknown API error"))
                raise EtherscanAPIError(f"Etherscan API error: {error_msg}")
            
            return data
            
        except httpx.HTTPError as e:
            raise EtherscanAPIError(f"HTTP request failed: {str(e)}")
        except Exception as e:
            raise EtherscanAPIError(f"Unexpected error: {str(e)}")


def api_call(params: Dict[str, Any]) -> str:
    """
    Make an API call and return formatted result as string.
    
    Args:
        params: Dictionary of API parameters
        
    Returns:
        JSON string of the API result
    """
    import asyncio
    import json
    
    # Run the async function in the current event loop or create one
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            # If we're in an async context, we need to handle this differently
            # For now, let's use a synchronous approach with httpx
            import httpx
            
            api_key = os.getenv("ETHERSCAN_API_KEY")
            if not api_key:
                raise EtherscanAPIError("ETHERSCAN_API_KEY environment variable is not set")
            
            # Build query parameters
            query_params = {}
            for key, value in params.items():
                if value is not None:
                    query_params[key] = str(value)
            
            query_params["apikey"] = api_key
            
            url = "https://api.etherscan.io/v2/api"
            
            with httpx.Client() as client:
                try:
                    response = client.get(url, params=query_params)
                    response.raise_for_status()
                    
                    data = response.json()
                    
                    # Check if API returned an error
                    if data.get("status") == "0" and data.get("message") != "No transactions found":
                        error_msg = data.get("result", data.get("message", "Unknown API error"))
                        raise EtherscanAPIError(f"Etherscan API error: {error_msg}")
                    
                    return json.dumps(data.get("result", data), indent=2)
                    
                except httpx.HTTPError as e:
                    raise EtherscanAPIError(f"HTTP request failed: {str(e)}")
                except Exception as e:
                    raise EtherscanAPIError(f"Unexpected error: {str(e)}")
        else:
            data = loop.run_until_complete(make_api_request(params))
            return json.dumps(data.get("result", data), indent=2)
    except RuntimeError:
        # No event loop, create one
        data = asyncio.run(make_api_request(params))
        return json.dumps(data.get("result", data), indent=2)


def format_response(data: Any) -> str:
    """Format API response data as JSON string."""
    import json
    return json.dumps(data, indent=2)


def filter_fields(data: Any, fields_to_remove: set = None) -> Any:
    """Filter out unnecessary fields from API response data for agent optimization.
    
    Args:
        data: The data to filter (dict, list, or primitive)
        fields_to_remove: Set of field names to remove
        
    Returns:
        Filtered data with unnecessary fields removed
    """
    if fields_to_remove is None:
        return data
        
    if isinstance(data, dict):
        return {k: filter_fields(v, fields_to_remove) 
                for k, v in data.items() 
                if k not in fields_to_remove}
    elif isinstance(data, list):
        return [filter_fields(item, fields_to_remove) for item in data]
    else:
        return data


def truncate_bytecode(data: Any, max_length: int = 2000) -> Any:
    """Truncate bytecode fields to manageable size for agents.
    
    Args:
        data: The data to process
        max_length: Maximum length for bytecode fields
        
    Returns:
        Data with truncated bytecode
    """
    if isinstance(data, str) and data.startswith('0x') and len(data) > max_length:
        return f"{data[:max_length]}...[truncated {len(data) - max_length} chars, total: {len(data)} chars]"
    return data


def api_call_filtered(params: Dict[str, Any], fields_to_remove: set = None) -> str:
    """
    Make an API call and return filtered result as string.
    
    Args:
        params: Dictionary of API parameters
        fields_to_remove: Set of field names to remove from response
        
    Returns:
        JSON string of the filtered API result
    """
    import asyncio
    import json
    
    # Run the async function in the current event loop or create one
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            # If we're in an async context, we need to handle this differently
            # For now, let's use a synchronous approach with httpx
            import httpx
            
            api_key = os.getenv("ETHERSCAN_API_KEY")
            if not api_key:
                raise EtherscanAPIError("ETHERSCAN_API_KEY environment variable is not set")
            
            # Build query parameters
            query_params = {}
            for key, value in params.items():
                if value is not None:
                    query_params[key] = str(value)
            
            query_params["apikey"] = api_key
            
            url = "https://api.etherscan.io/v2/api"
            
            with httpx.Client() as client:
                try:
                    response = client.get(url, params=query_params)
                    response.raise_for_status()
                    
                    data = response.json()
                    
                    # Check if API returned an error
                    if data.get("status") == "0" and data.get("message") != "No transactions found":
                        error_msg = data.get("result", data.get("message", "Unknown API error"))
                        raise EtherscanAPIError(f"Etherscan API error: {error_msg}")
                    
                    result = data.get("result", data)
                    if fields_to_remove:
                        result = filter_fields(result, fields_to_remove)
                    return json.dumps(result, indent=2)
                    
                except httpx.HTTPError as e:
                    raise EtherscanAPIError(f"HTTP request failed: {str(e)}")
                except Exception as e:
                    raise EtherscanAPIError(f"Unexpected error: {str(e)}")
        else:
            data = loop.run_until_complete(make_api_request(params))
            result = data.get("result", data)
            if fields_to_remove:
                result = filter_fields(result, fields_to_remove)
            return json.dumps(result, indent=2)
    except RuntimeError:
        # No event loop, create one
        data = asyncio.run(make_api_request(params))
        result = data.get("result", data)
        if fields_to_remove:
            result = filter_fields(result, fields_to_remove)
        return json.dumps(result, indent=2)


def api_call_with_bytecode_truncation(params: Dict[str, Any], max_bytecode_length: int = 2000) -> str:
    """
    Make an API call and return result with truncated bytecode for agent optimization.
    
    Args:
        params: Dictionary of API parameters
        max_bytecode_length: Maximum length for bytecode before truncation
        
    Returns:
        JSON string of the API result with truncated bytecode
    """
    import asyncio
    import json
    
    # Run the async function in the current event loop or create one
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            import httpx
            
            api_key = os.getenv("ETHERSCAN_API_KEY")
            if not api_key:
                raise EtherscanAPIError("ETHERSCAN_API_KEY environment variable is not set")
            
            # Build query parameters
            query_params = {}
            for key, value in params.items():
                if value is not None:
                    query_params[key] = str(value)
            
            query_params["apikey"] = api_key
            
            url = "https://api.etherscan.io/v2/api"
            
            with httpx.Client() as client:
                try:
                    response = client.get(url, params=query_params)
                    response.raise_for_status()
                    
                    data = response.json()
                    
                    # Check if API returned an error
                    if data.get("status") == "0" and data.get("message") != "No transactions found":
                        error_msg = data.get("result", data.get("message", "Unknown API error"))
                        raise EtherscanAPIError(f"Etherscan API error: {error_msg}")
                    
                    result = data.get("result", data)
                    # Truncate bytecode
                    result = truncate_bytecode(result, max_bytecode_length)
                    return json.dumps(result, indent=2)
                    
                except httpx.HTTPError as e:
                    raise EtherscanAPIError(f"HTTP request failed: {str(e)}")
                except Exception as e:
                    raise EtherscanAPIError(f"Unexpected error: {str(e)}")
        else:
            data = loop.run_until_complete(make_api_request(params))
            result = data.get("result", data)
            result = truncate_bytecode(result, max_bytecode_length)
            return json.dumps(result, indent=2)
    except RuntimeError:
        # No event loop, create one
        data = asyncio.run(make_api_request(params))
        result = data.get("result", data)
        result = truncate_bytecode(result, max_bytecode_length)
        return json.dumps(result, indent=2)


def create_tool_decorator(server: FastMCP):
    """Create a decorator for registering tools with the server."""
    def tool(name: str, description: str):
        def decorator(func):
            # The actual tool registration will be handled by the server setup
            func._tool_name = name
            func._tool_description = description
            return func
        return decorator
    return tool