"""Main MCP server implementation using FastMCP."""

import asyncio
import os
from mcp.server.fastmcp import FastMCP

# Import all tool modules
from .tools.accounts import register_account_tools
from .tools.blocks import register_block_tools
from .tools.contracts import register_contract_tools
from .tools.transactions import register_transaction_tools
from .tools.tokens import register_token_tools
from .tools.gas import register_gas_tools
from .tools.stats import register_stats_tools
from .tools.logs import register_logs_tools
from .tools.rpc import register_rpc_tools


def create_server() -> FastMCP:
    """Create and configure the FastMCP server with all tools."""
    
    # Create FastMCP server instance
    server = FastMCP("Etherscan MCP Python Server")
    
    # Register all tool categories
    register_account_tools(server)
    register_block_tools(server)
    register_contract_tools(server)
    register_transaction_tools(server)
    register_token_tools(server)
    register_gas_tools(server)
    register_stats_tools(server)
    register_logs_tools(server)
    register_rpc_tools(server)
    
    return server


def main():
    """Main function to run the MCP server."""
    # Check for API key
    if not os.getenv("ETHERSCAN_API_KEY"):
        import sys
        print("Warning: ETHERSCAN_API_KEY environment variable not set", file=sys.stderr, flush=True)
    
    # Create and run server
    server = create_server()
    
    # Run the server (stdio transport by default)
    server.run()


if __name__ == "__main__":
    main()