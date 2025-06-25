"""Statistics-related tools for Etherscan API."""

from mcp.server.fastmcp import FastMCP
from .utils import api_call


def register_stats_tools(server: FastMCP) -> None:
    """Register all statistics-related tools with the server."""
    
    @server.tool()
    def stats_ethsupply(chainid: str = "1") -> str:
        """Returns the current amount of Ether in circulation excluding ETH2 Staking rewards and EIP1559 burnt fees.
        
        Args:
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "stats",
            "action": "ethsupply",
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def stats_ethsupply2(chainid: str = "1") -> str:
        """Returns the current amount of Ether in circulation, ETH2 Staking rewards, EIP1559 burnt fees, and total withdrawn ETH from the beacon chain.
        
        Args:
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "stats",
            "action": "ethsupply2",
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def stats_ethprice(chainid: str = "1") -> str:
        """Returns the latest price of 1 ETH.
        
        Args:
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "stats",
            "action": "ethprice",
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def stats_chainsize(
        startdate: str, 
        enddate: str, 
        clienttype: str, 
        syncmode: str, 
        sort: str, 
        chainid: str = "1"
    ) -> str:
        """Returns the size of the Ethereum blockchain, in bytes, over a date range.
        
        Args:
            startdate: The starting date in yyyy-MM-dd format, eg. 2019-02-01
            enddate: The ending date in yyyy-MM-dd format, eg. 2019-02-28
            clienttype: The Ethereum node client to use, either `geth` or `parity`
            syncmode: The type of node to run, either `default` or `archive`
            sort: The sorting preference, use `asc` to sort by ascending and `desc` to sort by descending
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "stats",
            "action": "chainsize",
            "startdate": startdate,
            "enddate": enddate,
            "clienttype": clienttype,
            "syncmode": syncmode,
            "sort": sort,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def stats_nodecount(chainid: str = "1") -> str:
        """Returns the total number of discoverable Ethereum nodes.
        
        Args:
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "stats",
            "action": "nodecount",
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def stats_dailytxnfee(startdate: str, enddate: str, sort: str, chainid: str = "1") -> str:
        """Returns the amount of transaction fees paid to miners per day.
        
        Args:
            startdate: The starting date in yyyy-MM-dd format, eg. 2019-02-01
            enddate: The ending date in yyyy-MM-dd format, eg. 2019-02-28
            sort: The sorting preference, use `asc` to sort by ascending and `desc` to sort by descending
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "stats",
            "action": "dailytxnfee",
            "startdate": startdate,
            "enddate": enddate,
            "sort": sort,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def stats_dailynewaddress(startdate: str, enddate: str, sort: str, chainid: str = "1") -> str:
        """Returns the number of new Ethereum addresses created per day.
        
        Args:
            startdate: The starting date in yyyy-MM-dd format, eg. 2019-02-01
            enddate: The ending date in yyyy-MM-dd format, eg. 2019-02-28
            sort: The sorting preference, use `asc` to sort by ascending and `desc` to sort by descending
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "stats",
            "action": "dailynewaddress",
            "startdate": startdate,
            "enddate": enddate,
            "sort": sort,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def stats_dailynetutilization(startdate: str, enddate: str, sort: str, chainid: str = "1") -> str:
        """Returns the daily average gas used over gas limit, in percentage.
        
        Args:
            startdate: The starting date in yyyy-MM-dd format, eg. 2019-02-01
            enddate: The ending date in yyyy-MM-dd format, eg. 2019-02-28
            sort: The sorting preference, use `asc` to sort by ascending and `desc` to sort by descending
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "stats",
            "action": "dailynetutilization",
            "startdate": startdate,
            "enddate": enddate,
            "sort": sort,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def stats_dailyavghashrate(startdate: str, enddate: str, sort: str, chainid: str = "1") -> str:
        """Returns the historical measure of processing power of the Ethereum network.
        
        Args:
            startdate: The starting date in yyyy-MM-dd format, eg. 2019-02-01
            enddate: The ending date in yyyy-MM-dd format, eg. 2019-02-28
            sort: The sorting preference, use `asc` to sort by ascending and `desc` to sort by descending
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "stats",
            "action": "dailyavghashrate",
            "startdate": startdate,
            "enddate": enddate,
            "sort": sort,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def stats_dailytx(startdate: str, enddate: str, sort: str, chainid: str = "1") -> str:
        """Returns the number of transactions performed on the Ethereum blockchain per day.
        
        Args:
            startdate: The starting date in yyyy-MM-dd format, eg. 2019-02-01
            enddate: The ending date in yyyy-MM-dd format, eg. 2019-02-28
            sort: The sorting preference, use `asc` to sort by ascending and `desc` to sort by descending
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "stats",
            "action": "dailytx",
            "startdate": startdate,
            "enddate": enddate,
            "sort": sort,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def stats_dailyavgnetdifficulty(startdate: str, enddate: str, sort: str, chainid: str = "1") -> str:
        """Returns the historical mining difficulty of the Ethereum network.
        
        Args:
            startdate: The starting date in yyyy-MM-dd format, eg. 2019-02-01
            enddate: The ending date in yyyy-MM-dd format, eg. 2019-02-28
            sort: The sorting preference, use `asc` to sort by ascending and `desc` to sort by descending
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "stats",
            "action": "dailyavgnetdifficulty",
            "startdate": startdate,
            "enddate": enddate,
            "sort": sort,
            "chainid": chainid
        }
        return api_call(params)
    
    @server.tool()
    def stats_ethdailyprice(startdate: str, enddate: str, sort: str, chainid: str = "1") -> str:
        """Returns the historical price of 1 ETH.
        
        Args:
            startdate: The starting date in yyyy-MM-dd format, eg. 2019-02-01
            enddate: The ending date in yyyy-MM-dd format, eg. 2019-02-28
            sort: The sorting preference, use `asc` to sort by ascending and `desc` to sort by descending
            chainid: Chain id, default 1 (Ethereum)
        """
        params = {
            "module": "stats",
            "action": "ethdailyprice",
            "startdate": startdate,
            "enddate": enddate,
            "sort": sort,
            "chainid": chainid
        }
        return api_call(params)