"""
Configuration module for TradeBot.
"""

import os
from dataclasses import dataclass
from typing import Optional

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@dataclass
class TigerConfig:
    """Tiger Open Platform configuration."""
    tiger_id: str
    account: str
    private_key: str  # Changed from private_key_path to private_key
    market: str = "US"  # Default to US market
    language: str = "en_US"  # Default to English

def get_tiger_config() -> TigerConfig:
    """
    Get Tiger Open Platform configuration from environment variables.
    
    Returns:
        TigerConfig: Configuration object with Tiger API credentials
        
    Raises:
        ValueError: If required environment variables are not set
    """
    tiger_id = os.getenv("TIGER_ID")
    account = os.getenv("TIGER_ACCOUNT")
    private_key = os.getenv("TIGER_PRIVATE_KEY")
    
    if not all([tiger_id, account, private_key]):
        raise ValueError(
            "TIGER_ID, TIGER_ACCOUNT, and TIGER_PRIVATE_KEY environment variables must be set"
        )
    
    return TigerConfig(
        tiger_id=tiger_id,
        account=account,
        private_key=private_key
    ) 