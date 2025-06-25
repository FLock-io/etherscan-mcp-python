#!/usr/bin/env python3
"""Entry point for the Etherscan MCP Python server."""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.server import main

if __name__ == "__main__":
    main()