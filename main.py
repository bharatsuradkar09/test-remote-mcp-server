import random
from fastmcp import FastMCP
import json

mcp = FastMCP("Simple Calculator Server")

@mcp.tool
def add(a:int,b:int)->int:
    """
    Add two numbers together.

    Args:
    a:first number
    b:second number

    Return:
      The sum of a and b    
    """
    return a+b

@mcp.tool
def random_number(min_val:int=1,max_val:int=100)->int:
    """Generate a random number within a range.
     Args:
       min_val: Minimum value(default:1)
       max_val: Maximum value(default:100)

    Return:
      A random integer between min_val and max_val
    """
    return random.randint(min_val,max_val)

@mcp.resource("info://server")
def server_info()->str:
    """Get information about this server."""
    info = {
        "name" : "Simple Calculator Server",
        "version" : "1.0.0",
        "description" : "A basic MCP server with math tools",
        "tools" : ['add','random_number'],
        'author' : "your name"
    }
    return json.dumps(info,indent=2)


if __name__ == "__main__":
    mcp.run(transport='http',host="0.0.0.0",port=8000)
