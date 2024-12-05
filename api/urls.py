from dataclasses import dataclass
from enum import Enum


base_url = 'https://financialmodelingprep.com/api'


@dataclass
class URLInfo:
    """
    Dataclass for the API URLs
    """
    url: str
    description: str


class ApiUrlEnum(Enum):
    """
    Enum for the API URLs
    """
    STOCK_LIST = URLInfo(
        url = f'{base_url}/v3/stock/list',
        description = "Stock list"
    )
    ANNUAL_INCOME = URLInfo(
        url = f"{base_url}/v3/income-statement",
        description = "Annual income"
    )
    COMPANIES_PROFILE = URLInfo(
        url = f"{base_url}/v3/profile",
        description = "Companies profile"
    )
    BALANCE_SHEET = URLInfo(
        url = f"{base_url}/v3/balance-sheet-statement",
        description = "Balance sheet"
    )
    MARKET_CAPITALIZATION = URLInfo(
        url = f"{base_url}/v3/market-capitalization",
        description = "Market capitalization"
    )