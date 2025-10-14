"""Main MCP server implementation using FastMCP."""

import asyncio
import os
import argparse
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


def create_http_app():
    """Create and return ASGI application for HTTP deployment.

    Returns:
        Starlette application configured for Streamable HTTP transport
    """
    server = create_server()

    # Create HTTP app with Streamable HTTP transport (recommended for production)
    # Note: FastMCP's streamable_http_app() doesn't accept path parameter
    # The default MCP endpoint path is used
    return server.streamable_http_app()


def main():
    """Main function to run the MCP server with configurable transport."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Etherscan MCP Python Server")
    parser.add_argument(
        "--transport",
        type=str,
        choices=["stdio", "http"],
        default=os.getenv("MCP_TRANSPORT", "stdio"),
        help="Transport protocol to use (stdio or http). Default: stdio"
    )
    parser.add_argument(
        "--host",
        type=str,
        default=os.getenv("MCP_HOST", "127.0.0.1"),
        help="Host to bind HTTP server (only for http transport). Default: 127.0.0.1"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.getenv("MCP_PORT", "8000")),
        help="Port to bind HTTP server (only for http transport). Default: 8000"
    )

    args = parser.parse_args()

    # Check for API key
    if not os.getenv("ETHERSCAN_API_KEY"):
        import sys
        print("Warning: ETHERSCAN_API_KEY environment variable not set", file=sys.stderr, flush=True)

    # Create and run server
    server = create_server()

    # Run the server with specified transport
    if args.transport == "http":
        print(f"Starting Etherscan MCP server with HTTP transport on {args.host}:{args.port}", flush=True)
        print(f"Server URL: http://{args.host}:{args.port}/mcp", flush=True)
        server.run(transport="http", host=args.host, port=args.port)
    else:
        # Default: stdio transport
        server.run()


if __name__ == "__main__":
    main()