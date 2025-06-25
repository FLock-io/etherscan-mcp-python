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