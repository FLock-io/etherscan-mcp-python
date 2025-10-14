#!/usr/bin/env python3
"""
HTTP Server entry point for Etherscan MCP Python Server.

This module provides an ASGI application for deploying the Etherscan MCP server
via HTTP using Streamable HTTP transport. It can be run directly or with ASGI
servers like Uvicorn.

Usage:
    # Direct run (development)
    python http_server.py

    # With Uvicorn (production)
    uvicorn http_server:app --host 0.0.0.0 --port 8000

    # With workers for better concurrency
    uvicorn http_server:app --host 0.0.0.0 --port 8000 --workers 4

    # With environment variables
    MCP_HOST=0.0.0.0 MCP_PORT=8080 python http_server.py
"""

import os
import sys

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # If python-dotenv is not installed, continue without it
    pass

from src.server import create_http_app

# Create ASGI application
# This app variable will be used by Uvicorn or other ASGI servers
app = create_http_app()


def main():
    """Run the HTTP server directly using Uvicorn."""
    try:
        import uvicorn
    except ImportError:
        print("Error: uvicorn is not installed. Install it with:")
        print("  pip install uvicorn[standard]")
        print("  or: uv pip install uvicorn[standard]")
        sys.exit(1)

    # Check for API key
    if not os.getenv("ETHERSCAN_API_KEY"):
        print("Warning: ETHERSCAN_API_KEY environment variable not set", file=sys.stderr, flush=True)

    # Get configuration from environment variables
    host = os.getenv("MCP_HOST", "127.0.0.1")
    port = int(os.getenv("MCP_PORT", "8000"))
    log_level = os.getenv("MCP_LOG_LEVEL", "info")

    print(f"Starting Etherscan MCP HTTP Server", flush=True)
    print(f"Server URL: http://{host}:{port}/mcp", flush=True)
    print(f"Log level: {log_level}", flush=True)
    print(f"\nPress CTRL+C to stop the server\n", flush=True)

    # Run the server
    uvicorn.run(
        app,
        host=host,
        port=port,
        log_level=log_level,
        access_log=True
    )


if __name__ == "__main__":
    main()
