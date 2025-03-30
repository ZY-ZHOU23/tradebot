"""
Test cases for the main module and Tiger API connection.
"""
# %%
import os
import sys
import pytest
from dotenv import load_dotenv

from tradebot.main import main
from tradebot.config import TigerConfig, get_tiger_config
from tradebot.tiger_client import TigerClient

# Load environment variables
load_dotenv()

# %%
# Interactive Testing Cell
def test_tiger_connection_interactive():
    """Interactive test for Tiger API connection."""
    # Get credentials from environment
    tiger_id = os.getenv("TIGER_ID")
    account = os.getenv("TIGER_ACCOUNT")
    private_key = os.getenv("TIGER_PRIVATE_KEY")
    
    if not all([tiger_id, account, private_key]):
        print("Error: TIGER_ID, TIGER_ACCOUNT, and TIGER_PRIVATE_KEY must be set in .env file")
        return
    
    print(f"Using Tiger ID: {tiger_id}")
    print(f"Using Account: {account}")
    print("Testing connection...")
    
    # Create and test client
    config = TigerConfig(
        tiger_id=tiger_id,
        account=account,
        private_key=private_key
    )
    client = TigerClient(config)
    
    # Test connection
    success = client.connect()
    print(f"Connection {'successful' if success else 'failed'}")
    
    if success:
        print("Testing disconnection...")
        client.disconnect()
        print("Disconnected successfully")

# %%
# Automated Tests
def test_tiger_config():
    """Test Tiger API configuration loading."""
    config = get_tiger_config()
    assert isinstance(config, TigerConfig)
    assert config.tiger_id is not None
    assert config.account is not None
    assert config.private_key is not None
    assert config.market == "US"
    assert config.language == "en_US"

def test_tiger_connection():
    """Test Tiger API connection."""
    config = get_tiger_config()
    client = TigerClient(config)
    
    # Test connection
    assert client.connect() is True
    assert client.is_connected() is True
    
    # Test disconnection
    client.disconnect()
    assert client.is_connected() is False

def test_main():
    """Test that main function returns 0 on successful execution."""
    assert main() == 0

# %%
# Run interactive test if executed directly
if __name__ == "__main__":
    test_tiger_connection_interactive() 

 
# %%
