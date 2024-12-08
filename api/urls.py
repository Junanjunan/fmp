from dataclasses import dataclass
from enum import Enum


base_url = 'https://financialmodelingprep.com/api'


@dataclass
class URLInfo:
    """
    Dataclass for the API URLs
    """
    url: str
    usage: str
    description: str
    docs: str


class ApiUrlEnum(Enum):
    """
    Enum for the API URLs
    """
    STOCK_LIST = URLInfo(
        url = f'{base_url}/v3/stock/list',
        usage = "https://financialmodelingprep.com/api/v3/stock/list?apikey=YOUR_API_KEY",
        description = "Stock list",
        docs = "https://site.financialmodelingprep.com/developer/docs#symbol-list-stock-list",
    )
    ANNUAL_INCOME = URLInfo(
        url = f"{base_url}/v3/income-statement",
        usage = """
        https://financialmodelingprep.com/api/v3/income-statement/AAPL?period=annual&apikey=YOUR_API_KEY
        https://financialmodelingprep.com/api/v3/income-statement/AAPL?period=quarter&apikey=YOUR_API_KEY
        """,
        description = "Annual income",
        docs = "https://site.financialmodelingprep.com/developer/docs#income-statements-financial-statements",
    )
    COMPANIES_PROFILE = URLInfo(
        url = f"{base_url}/v3/profile",
        usage = "https://financialmodelingprep.com/api/v3/profile/AAPL?apikey=YOUR_API_KEY",
        description = "Companies profile",
        docs = "https://site.financialmodelingprep.com/developer/docs#company-profile-company-information",
    )
    BALANCE_SHEET = URLInfo(
        url = f"{base_url}/v3/balance-sheet-statement",
        usage = """
        https://financialmodelingprep.com/api/v3/balance-sheet-statement/AAPL?period=annual&apikey=YOUR_API_KEY
        https://financialmodelingprep.com/api/v3/balance-sheet-statement/AAPL?period=quarter&apikey=YOUR_API_KEY
        """,
        description = "Balance sheet",
        docs = "https://site.financialmodelingprep.com/developer/docs#balance-sheet-statements-financial-statements",
    )
    MARKET_CAPITALIZATION = URLInfo(
        url = f"{base_url}/v3/market-capitalization",
        usage = "https://financialmodelingprep.com/api/v3/market-capitalization/AAPL?apikey=YOUR_API_KEY",
        description = "Market capitalization",
        docs = "https://site.financialmodelingprep.com/developer/docs#market-cap-company-information",
    )