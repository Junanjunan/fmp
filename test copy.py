import pandas as pd
import requests

BASE_URL = "https://financialmodelingprep.com/"

API_KEY = "sdds"

"""Annual income statements"""

# annual_income_url = api/v3/income-statement/AAPL?apikey=

ANNUAL_INCOME_URL = "https://financialmodelingprep.com/api/v3/income-statement/{}?apikey="

tikcer_list = ['AAPL', 'TSLA']

annual_income_url = ANNUAL_INCOME_URL.format("AAPL") + API_KEY
# pd_AAPL = pd.read_json(AAPL_url)

# pd_AAPL.to_excel('AAPL.xlsx')

req_annual_income_url = requests.get(annual_income_url)
res_annual_income_url = req_annual_income_url.json()
# print(req_stock_fundamentals.json()[0]['date'])
# print(req_stock_fundamentals.json()[1]['date'])



URL_COMPANIES_PROFILE = "https://financialmodelingprep.com/api/v3/profile/{}?apikey="
companies_profile_url = URL_COMPANIES_PROFILE.format("AAPL") + API_KEY
req_companies_profile = requests.get(companies_profile_url)
res_companies_profile = req_companies_profile.json()

URL_BALANCE_SHEET = 'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{}?apikey='
url_balance_sheet = URL_BALANCE_SHEET.format('AAPL') + API_KEY
req_url_balance_sheet = requests.get(url_balance_sheet)
res_url_balance_sheet = req_url_balance_sheet.json()

URL_MARKET_CAPITALIZATION = 'https://financialmodelingprep.com/api/v3/market-capitalization/{}?apikey='
url_market_capitalization = URL_MARKET_CAPITALIZATION.format("AAPL") + API_KEY
req_url_market_capitalization = requests.get(url_market_capitalization)
res_url_market_capitalization = req_url_market_capitalization.json()


# URL_SHARE_FLOAT = 'https://financialmodelingprep.com/api/v4/shares_float?{}?apikey='    # {"Error Message" : "Special Endpoint : this endpoint is only for premium members please visit our subscription page to upgrade your plan at https://financialmodelingprep.com/developer/docs/pricing"}
# url_share_float = URL_SHARE_FLOAT.format('AAPL') + API_KEY
# req_url_share_float = requests.get(url_share_float)
# res_url_share_float = req_url_share_float.json()



symbol = res_annual_income_url[0]['symbol']
company_name = res_companies_profile[0]['companyName']
exchange = res_companies_profile[0]['exchangeShortName']
country = res_companies_profile[0]['country']
price = res_companies_profile[0]['price']
# market_cap = res_companies_profile[0]['mktCap']
market_cap = res_url_market_capitalization[0]['marketCap']
stock_count = int(market_cap)/int(price)
# outstanding_shares = res_url_share_float[0]['outstandingShares']
revenue = res_annual_income_url[0]['revenue'] # 매출 0, 1, 2, 3, 4
cost_of_revenue = res_annual_income_url[0]['costOfRevenue'] # 매출 원가 0, 1, 2, 3, 4
gross_profit = res_annual_income_url[0]['grossProfit'] # 순매출 0, 1, 2, 3, 4
gorss_profit_ratio = res_annual_income_url[0]['grossProfitRatio'] # 매출 이익률? 0, 1, 2, 3, 4
operating_income = res_annual_income_url[0]['operatingIncome'] # 영업이익 0, 1, 2, 3, 4
# operating_expenses = res_annual_income_url[0]['operatingExpenses'] # 영업 비용 0, 1, 2, 3, 4
operating_income_ratio = res_annual_income_url[0]['operatingIncomeRatio'] # 영업이익률 0, 1, 2, 3, 4
net_income = res_annual_income_url[0]['netIncome'] # 당기순이익 0, 1, 2, 3, 4
net_income_ratio = res_annual_income_url[0]['netIncomeRatio'] # 당기순이익률 0, 1, 2, 3, 4
eps = res_annual_income_url[0]['eps'] # 0, 1, 2, 3, 4
total_assets = res_url_balance_sheet[0]['totalAssets'] # 0, 1, 2, 3, 4
total_liabilities = res_url_balance_sheet[0]['totalLiabilities'] # 0, 1, 2, 3, 4
net_assets = float(total_assets) - float(total_liabilities)
net_assets_ratio = float(net_income)/net_assets
link1 = res_annual_income_url[0]['link'] # 0, 1, 2, 3, 4
link2 = res_annual_income_url[0]['finalLink'] # 0, 1, 2, 3, 4


print(symbol)
print(company_name)
print(exchange)
print(country)
print(price)
print(market_cap)
print(stock_count)
print(revenue)
print(cost_of_revenue)
print(gross_profit)
print(gorss_profit_ratio)
print(operating_income)
# print(operating_expenses)
print(operating_income_ratio)
print(net_income)
print(net_income_ratio)
print(eps)

print(total_assets)
print(total_liabilities)
print(net_assets)
print(net_assets_ratio)

print(link1)
print(link2)

df1 = pd.DataFrame([
    {
    'symbol': symbol,
    'company_name': company_name,
    'exchange': exchange,
    'country': country,
    'price': price,
    'market_cap': market_cap,
    'stock_count': stock_count,
    'revenue': revenue,
    'cost_of_revenue': cost_of_revenue,
    'gross_profit': gross_profit,
    'gorss_profit_ratio': gorss_profit_ratio,
    'operating_income': operating_income,
    'operating_income_ratio': operating_income_ratio,
    'net_income': net_income,
    'net_income_ratio': net_income_ratio,
    'eps': eps,
    'total_assets': total_assets,
    'total_liabilities': total_liabilities,
    'net_assets': net_assets,
    'net_assets_ratio': net_assets_ratio,
    'link1': link1,
    'link2': link2,
    }
])


df1.to_excel('oh.xlsx')






# for i in ticker_list:
