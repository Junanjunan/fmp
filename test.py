import pandas as pd
import requests

BASE_URL = "https://financialmodelingprep.com/"

API_KEY = "1a577e3ab9a75af1372c780a58963858"

ANNUAL_INCOME_URL = "https://financialmodelingprep.com/api/v3/income-statement/{}?apikey="
URL_COMPANIES_PROFILE = "https://financialmodelingprep.com/api/v3/profile/{}?apikey="
URL_BALANCE_SHEET = 'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{}?apikey='
URL_MARKET_CAPITALIZATION = 'https://financialmodelingprep.com/api/v3/market-capitalization/{}?apikey='

csv1 = pd.read_csv('01.csv')
csv2 = pd.read_csv('02.csv')
csv3 = pd.read_csv('03.csv')

csv1_list = list(csv1['Symbol'])
csv2_list = list(csv2['Symbol'])
csv3_list = list(csv3['Symbol'])

csv1_list.extend(csv2_list)
csv1_list.extend(csv3_list)


ticker_list = csv1_list

df = pd.DataFrame()


for i in ticker_list:
    try:
        annual_income_url = ANNUAL_INCOME_URL.format(i) + API_KEY
        req_annual_income_url = requests.get(annual_income_url)
        res_annual_income_url = req_annual_income_url.json()

        companies_profile_url = URL_COMPANIES_PROFILE.format(i) + API_KEY
        req_companies_profile = requests.get(companies_profile_url)
        res_companies_profile = req_companies_profile.json()

        url_balance_sheet = URL_BALANCE_SHEET.format(i) + API_KEY
        req_url_balance_sheet = requests.get(url_balance_sheet)
        res_url_balance_sheet = req_url_balance_sheet.json()

        
        url_market_capitalization = URL_MARKET_CAPITALIZATION.format(i) + API_KEY
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


        if res_annual_income_url[4]['revenue']:
            revenue0 = res_annual_income_url[0]['revenue'] # 매출 0, 1, 2, 3, 4
            revenue1 = res_annual_income_url[1]['revenue'] # 매출 0, 1, 2, 3, 4
            revenue2 = res_annual_income_url[2]['revenue'] # 매출 0, 1, 2, 3, 4
            revenue3 = res_annual_income_url[3]['revenue'] # 매출 0, 1, 2, 3, 4
            revenue4 = res_annual_income_url[4]['revenue'] # 매출 0, 1, 2, 3, 4
            cost_of_revenue0 = res_annual_income_url[0]['costOfRevenue'] # 매출 원가 0, 1, 2, 3, 4
            cost_of_revenue1 = res_annual_income_url[1]['costOfRevenue'] # 매출 원가 0, 1, 2, 3, 4
            cost_of_revenue2 = res_annual_income_url[2]['costOfRevenue'] # 매출 원가 0, 1, 2, 3, 4
            cost_of_revenue3 = res_annual_income_url[3]['costOfRevenue'] # 매출 원가 0, 1, 2, 3, 4
            cost_of_revenue4 = res_annual_income_url[4]['costOfRevenue'] # 매출 원가 0, 1, 2, 3, 4
            gross_profit0 = res_annual_income_url[0]['grossProfit'] # 순매출 0, 1, 2, 3, 4
            gross_profit1 = res_annual_income_url[1]['grossProfit'] # 순매출 0, 1, 2, 3, 4
            gross_profit2 = res_annual_income_url[2]['grossProfit'] # 순매출 0, 1, 2, 3, 4
            gross_profit3 = res_annual_income_url[3]['grossProfit'] # 순매출 0, 1, 2, 3, 4
            gross_profit4 = res_annual_income_url[4]['grossProfit'] # 순매출 0, 1, 2, 3, 4
            gross_profit_ratio0 = res_annual_income_url[0]['grossProfitRatio'] # 매출 이익률? 0, 1, 2, 3, 4
            gross_profit_ratio1 = res_annual_income_url[1]['grossProfitRatio'] # 매출 이익률? 0, 1, 2, 3, 4
            gross_profit_ratio2 = res_annual_income_url[2]['grossProfitRatio'] # 매출 이익률? 0, 1, 2, 3, 4
            gross_profit_ratio3 = res_annual_income_url[3]['grossProfitRatio'] # 매출 이익률? 0, 1, 2, 3, 4
            gross_profit_ratio4 = res_annual_income_url[4]['grossProfitRatio'] # 매출 이익률? 0, 1, 2, 3, 4
            operating_income0 = res_annual_income_url[0]['operatingIncome'] # 영업이익 0, 1, 2, 3, 4
            operating_income1 = res_annual_income_url[1]['operatingIncome'] # 영업이익 0, 1, 2, 3, 4
            operating_income2 = res_annual_income_url[2]['operatingIncome'] # 영업이익 0, 1, 2, 3, 4
            operating_income3 = res_annual_income_url[3]['operatingIncome'] # 영업이익 0, 1, 2, 3, 4
            operating_income4 = res_annual_income_url[4]['operatingIncome'] # 영업이익 0, 1, 2, 3, 4
            # operating_expenses = res_annual_income_url[0]['operatingExpenses'] # 영업 비용 0, 1, 2, 3, 4
            operating_income_ratio0 = res_annual_income_url[0]['operatingIncomeRatio'] # 영업이익률 0, 1, 2, 3, 4
            operating_income_ratio1 = res_annual_income_url[1]['operatingIncomeRatio'] # 영업이익률 0, 1, 2, 3, 4
            operating_income_ratio2 = res_annual_income_url[2]['operatingIncomeRatio'] # 영업이익률 0, 1, 2, 3, 4
            operating_income_ratio3 = res_annual_income_url[3]['operatingIncomeRatio'] # 영업이익률 0, 1, 2, 3, 4
            operating_income_ratio4 = res_annual_income_url[4]['operatingIncomeRatio'] # 영업이익률 0, 1, 2, 3, 4
            net_income0 = res_annual_income_url[0]['netIncome'] # 당기순이익 0, 1, 2, 3, 4
            net_income1 = res_annual_income_url[1]['netIncome'] # 당기순이익 0, 1, 2, 3, 4
            net_income2 = res_annual_income_url[2]['netIncome'] # 당기순이익 0, 1, 2, 3, 4
            net_income3 = res_annual_income_url[3]['netIncome'] # 당기순이익 0, 1, 2, 3, 4
            net_income4 = res_annual_income_url[4]['netIncome'] # 당기순이익 0, 1, 2, 3, 4
            net_income_ratio0 = res_annual_income_url[0]['netIncomeRatio'] # 당기순이익률 0, 1, 2, 3, 4
            net_income_ratio1 = res_annual_income_url[1]['netIncomeRatio'] # 당기순이익률 0, 1, 2, 3, 4
            net_income_ratio2 = res_annual_income_url[2]['netIncomeRatio'] # 당기순이익률 0, 1, 2, 3, 4
            net_income_ratio3 = res_annual_income_url[3]['netIncomeRatio'] # 당기순이익률 0, 1, 2, 3, 4
            net_income_ratio4 = res_annual_income_url[4]['netIncomeRatio'] # 당기순이익률 0, 1, 2, 3, 4
            eps0 = res_annual_income_url[0]['eps'] # 0, 1, 2, 3, 4
            eps1 = res_annual_income_url[1]['eps'] # 0, 1, 2, 3, 4
            eps2 = res_annual_income_url[2]['eps'] # 0, 1, 2, 3, 4
            eps3 = res_annual_income_url[3]['eps'] # 0, 1, 2, 3, 4
            eps4 = res_annual_income_url[4]['eps'] # 0, 1, 2, 3, 4
            total_assets0 = res_url_balance_sheet[0]['totalAssets'] # 0, 1, 2, 3, 4
            total_assets1 = res_url_balance_sheet[1]['totalAssets'] # 0, 1, 2, 3, 4
            total_assets2 = res_url_balance_sheet[2]['totalAssets'] # 0, 1, 2, 3, 4
            total_assets3 = res_url_balance_sheet[3]['totalAssets'] # 0, 1, 2, 3, 4
            total_assets4 = res_url_balance_sheet[4]['totalAssets'] # 0, 1, 2, 3, 4
            total_liabilities0 = res_url_balance_sheet[0]['totalLiabilities'] # 0, 1, 2, 3, 4
            total_liabilities1 = res_url_balance_sheet[1]['totalLiabilities'] # 0, 1, 2, 3, 4
            total_liabilities2 = res_url_balance_sheet[2]['totalLiabilities'] # 0, 1, 2, 3, 4
            total_liabilities3 = res_url_balance_sheet[3]['totalLiabilities'] # 0, 1, 2, 3, 4
            total_liabilities4 = res_url_balance_sheet[4]['totalLiabilities'] # 0, 1, 2, 3, 4
            net_assets0 = float(total_assets0) - float(total_liabilities0)
            net_assets1 = float(total_assets1) - float(total_liabilities1)
            net_assets2 = float(total_assets2) - float(total_liabilities2)
            net_assets3 = float(total_assets3) - float(total_liabilities3)
            net_assets4 = float(total_assets4) - float(total_liabilities4)
            if net_assets0 != 0:
                net_assets_ratio0 = float(net_income0)/net_assets0
            else:
                net_assets_ratio0 = "."
            if net_assets1 != 0:
                net_assets_ratio1 = float(net_income1)/net_assets1
            else:
                net_assets_ratio1 = "."
            if net_assets2 != 0:
                net_assets_ratio2 = float(net_income2)/net_assets2
            else:
                net_assets_ratio2 = "."
            if net_assets3 != 0:
                net_assets_ratio3 = float(net_income3)/net_assets3
            else:
                net_assets_ratio3 = "."
            if net_assets4 != 0:
                net_assets_ratio4 = float(net_income4)/net_assets4
            else:
                net_assets_ratio4 = "."
        
        elif res_annual_income_url[3]['revenue']:
            revenue0 = res_annual_income_url[0]['revenue'] # 매출 0, 1, 2, 3, 4
            revenue1 = res_annual_income_url[1]['revenue'] # 매출 0, 1, 2, 3, 4
            revenue2 = res_annual_income_url[2]['revenue'] # 매출 0, 1, 2, 3, 4
            revenue3 = res_annual_income_url[3]['revenue'] # 매출 0, 1, 2, 3, 4
            cost_of_revenue0 = res_annual_income_url[0]['costOfRevenue'] # 매출 원가 0, 1, 2, 3, 4
            cost_of_revenue1 = res_annual_income_url[1]['costOfRevenue'] # 매출 원가 0, 1, 2, 3, 4
            cost_of_revenue2 = res_annual_income_url[2]['costOfRevenue'] # 매출 원가 0, 1, 2, 3, 4
            cost_of_revenue3 = res_annual_income_url[3]['costOfRevenue'] # 매출 원가 0, 1, 2, 3, 4
            gross_profit0 = res_annual_income_url[0]['grossProfit'] # 순매출 0, 1, 2, 3, 4
            gross_profit1 = res_annual_income_url[1]['grossProfit'] # 순매출 0, 1, 2, 3, 4
            gross_profit2 = res_annual_income_url[2]['grossProfit'] # 순매출 0, 1, 2, 3, 4
            gross_profit3 = res_annual_income_url[3]['grossProfit'] # 순매출 0, 1, 2, 3, 4
            gross_profit_ratio0 = res_annual_income_url[0]['grossProfitRatio'] # 매출 이익률? 0, 1, 2, 3, 4
            gross_profit_ratio1 = res_annual_income_url[1]['grossProfitRatio'] # 매출 이익률? 0, 1, 2, 3, 4
            gross_profit_ratio2 = res_annual_income_url[2]['grossProfitRatio'] # 매출 이익률? 0, 1, 2, 3, 4
            gross_profit_ratio3 = res_annual_income_url[3]['grossProfitRatio'] # 매출 이익률? 0, 1, 2, 3, 4
            operating_income0 = res_annual_income_url[0]['operatingIncome'] # 영업이익 0, 1, 2, 3, 4
            operating_income1 = res_annual_income_url[1]['operatingIncome'] # 영업이익 0, 1, 2, 3, 4
            operating_income2 = res_annual_income_url[2]['operatingIncome'] # 영업이익 0, 1, 2, 3, 4
            operating_income3 = res_annual_income_url[3]['operatingIncome'] # 영업이익 0, 1, 2, 3, 4
            # operating_expenses = res_annual_income_url[0]['operatingExpenses'] # 영업 비용 0, 1, 2, 3, 4
            operating_income_ratio0 = res_annual_income_url[0]['operatingIncomeRatio'] # 영업이익률 0, 1, 2, 3, 4
            operating_income_ratio1 = res_annual_income_url[1]['operatingIncomeRatio'] # 영업이익률 0, 1, 2, 3, 4
            operating_income_ratio2 = res_annual_income_url[2]['operatingIncomeRatio'] # 영업이익률 0, 1, 2, 3, 4
            operating_income_ratio3 = res_annual_income_url[3]['operatingIncomeRatio'] # 영업이익률 0, 1, 2, 3, 4
            net_income0 = res_annual_income_url[0]['netIncome'] # 당기순이익 0, 1, 2, 3, 4
            net_income1 = res_annual_income_url[1]['netIncome'] # 당기순이익 0, 1, 2, 3, 4
            net_income2 = res_annual_income_url[2]['netIncome'] # 당기순이익 0, 1, 2, 3, 4
            net_income3 = res_annual_income_url[3]['netIncome'] # 당기순이익 0, 1, 2, 3, 4
            net_income_ratio0 = res_annual_income_url[0]['netIncomeRatio'] # 당기순이익률 0, 1, 2, 3, 4
            net_income_ratio1 = res_annual_income_url[1]['netIncomeRatio'] # 당기순이익률 0, 1, 2, 3, 4
            net_income_ratio2 = res_annual_income_url[2]['netIncomeRatio'] # 당기순이익률 0, 1, 2, 3, 4
            net_income_ratio3 = res_annual_income_url[3]['netIncomeRatio'] # 당기순이익률 0, 1, 2, 3, 4
            eps0 = res_annual_income_url[0]['eps'] # 0, 1, 2, 3, 4
            eps1 = res_annual_income_url[1]['eps'] # 0, 1, 2, 3, 4
            eps2 = res_annual_income_url[2]['eps'] # 0, 1, 2, 3, 4
            eps3 = res_annual_income_url[3]['eps'] # 0, 1, 2, 3, 4
            total_assets0 = res_url_balance_sheet[0]['totalAssets'] # 0, 1, 2, 3, 4
            total_assets1 = res_url_balance_sheet[1]['totalAssets'] # 0, 1, 2, 3, 4
            total_assets2 = res_url_balance_sheet[2]['totalAssets'] # 0, 1, 2, 3, 4
            total_assets3 = res_url_balance_sheet[3]['totalAssets'] # 0, 1, 2, 3, 4
            total_liabilities0 = res_url_balance_sheet[0]['totalLiabilities'] # 0, 1, 2, 3, 4
            total_liabilities1 = res_url_balance_sheet[1]['totalLiabilities'] # 0, 1, 2, 3, 4
            total_liabilities2 = res_url_balance_sheet[2]['totalLiabilities'] # 0, 1, 2, 3, 4
            total_liabilities3 = res_url_balance_sheet[3]['totalLiabilities'] # 0, 1, 2, 3, 4
            net_assets0 = float(total_assets0) - float(total_liabilities0)
            net_assets1 = float(total_assets1) - float(total_liabilities1)
            net_assets2 = float(total_assets2) - float(total_liabilities2)
            net_assets3 = float(total_assets3) - float(total_liabilities3)
            if net_assets0 != 0:
                net_assets_ratio0 = float(net_income0)/net_assets0
            else:
                net_assets_ratio0 = "."
            if net_assets1 != 0:
                net_assets_ratio1 = float(net_income1)/net_assets1
            else:
                net_assets_ratio1 = "."
            if net_assets2 != 0:
                net_assets_ratio2 = float(net_income2)/net_assets2
            else:
                net_assets_ratio2 = "."
            if net_assets3 != 0:
                net_assets_ratio3 = float(net_income3)/net_assets3
            else:
                net_assets_ratio3 = "."

        elif res_annual_income_url[2]['revenue']:
            revenue0 = res_annual_income_url[0]['revenue'] # 매출 0, 1, 2, 3, 4
            revenue1 = res_annual_income_url[1]['revenue'] # 매출 0, 1, 2, 3, 4
            revenue2 = res_annual_income_url[2]['revenue'] # 매출 0, 1, 2, 3, 4
            cost_of_revenue0 = res_annual_income_url[0]['costOfRevenue'] # 매출 원가 0, 1, 2, 3, 4
            cost_of_revenue1 = res_annual_income_url[1]['costOfRevenue'] # 매출 원가 0, 1, 2, 3, 4
            cost_of_revenue2 = res_annual_income_url[2]['costOfRevenue'] # 매출 원가 0, 1, 2, 3, 4
            gross_profit0 = res_annual_income_url[0]['grossProfit'] # 순매출 0, 1, 2, 3, 4
            gross_profit1 = res_annual_income_url[1]['grossProfit'] # 순매출 0, 1, 2, 3, 4
            gross_profit2 = res_annual_income_url[2]['grossProfit'] # 순매출 0, 1, 2, 3, 4
            gross_profit_ratio0 = res_annual_income_url[0]['grossProfitRatio'] # 매출 이익률? 0, 1, 2, 3, 4
            gross_profit_ratio1 = res_annual_income_url[1]['grossProfitRatio'] # 매출 이익률? 0, 1, 2, 3, 4
            gross_profit_ratio2 = res_annual_income_url[2]['grossProfitRatio'] # 매출 이익률? 0, 1, 2, 3, 4
            operating_income0 = res_annual_income_url[0]['operatingIncome'] # 영업이익 0, 1, 2, 3, 4
            operating_income1 = res_annual_income_url[1]['operatingIncome'] # 영업이익 0, 1, 2, 3, 4
            operating_income2 = res_annual_income_url[2]['operatingIncome'] # 영업이익 0, 1, 2, 3, 4
            # operating_expenses = res_annual_income_url[0]['operatingExpenses'] # 영업 비용 0, 1, 2, 3, 4
            operating_income_ratio0 = res_annual_income_url[0]['operatingIncomeRatio'] # 영업이익률 0, 1, 2, 3, 4
            operating_income_ratio1 = res_annual_income_url[1]['operatingIncomeRatio'] # 영업이익률 0, 1, 2, 3, 4
            operating_income_ratio2 = res_annual_income_url[2]['operatingIncomeRatio'] # 영업이익률 0, 1, 2, 3, 4
            net_income0 = res_annual_income_url[0]['netIncome'] # 당기순이익 0, 1, 2, 3, 4
            net_income1 = res_annual_income_url[1]['netIncome'] # 당기순이익 0, 1, 2, 3, 4
            net_income2 = res_annual_income_url[2]['netIncome'] # 당기순이익 0, 1, 2, 3, 4
            net_income_ratio0 = res_annual_income_url[0]['netIncomeRatio'] # 당기순이익률 0, 1, 2, 3, 4
            net_income_ratio1 = res_annual_income_url[1]['netIncomeRatio'] # 당기순이익률 0, 1, 2, 3, 4
            net_income_ratio2 = res_annual_income_url[2]['netIncomeRatio'] # 당기순이익률 0, 1, 2, 3, 4
            eps0 = res_annual_income_url[0]['eps'] # 0, 1, 2, 3, 4
            eps1 = res_annual_income_url[1]['eps'] # 0, 1, 2, 3, 4
            eps2 = res_annual_income_url[2]['eps'] # 0, 1, 2, 3, 4
            total_assets0 = res_url_balance_sheet[0]['totalAssets'] # 0, 1, 2, 3, 4
            total_assets1 = res_url_balance_sheet[1]['totalAssets'] # 0, 1, 2, 3, 4
            total_assets2 = res_url_balance_sheet[2]['totalAssets'] # 0, 1, 2, 3, 4
            total_liabilities0 = res_url_balance_sheet[0]['totalLiabilities'] # 0, 1, 2, 3, 4
            total_liabilities1 = res_url_balance_sheet[1]['totalLiabilities'] # 0, 1, 2, 3, 4
            total_liabilities2 = res_url_balance_sheet[2]['totalLiabilities'] # 0, 1, 2, 3, 4
            net_assets0 = float(total_assets0) - float(total_liabilities0)
            net_assets1 = float(total_assets1) - float(total_liabilities1)
            net_assets2 = float(total_assets2) - float(total_liabilities2)
            if net_assets0 != 0:
                net_assets_ratio0 = float(net_income0)/net_assets0
            else:
                net_assets_ratio0 = "."
            if net_assets1 != 0:
                net_assets_ratio1 = float(net_income1)/net_assets1
            else:
                net_assets_ratio1 = "."
            if net_assets2 != 0:
                net_assets_ratio2 = float(net_income2)/net_assets2
            else:
                net_assets_ratio2 = "."

        elif res_annual_income_url[1]['revenue']:
            revenue0 = res_annual_income_url[0]['revenue'] # 매출 0, 1, 2, 3, 4
            revenue1 = res_annual_income_url[1]['revenue'] # 매출 0, 1, 2, 3, 4
            cost_of_revenue0 = res_annual_income_url[0]['costOfRevenue'] # 매출 원가 0, 1, 2, 3, 4
            cost_of_revenue1 = res_annual_income_url[1]['costOfRevenue'] # 매출 원가 0, 1, 2, 3, 4
            gross_profit0 = res_annual_income_url[0]['grossProfit'] # 순매출 0, 1, 2, 3, 4
            gross_profit1 = res_annual_income_url[1]['grossProfit'] # 순매출 0, 1, 2, 3, 4
            gross_profit_ratio0 = res_annual_income_url[0]['grossProfitRatio'] # 매출 이익률? 0, 1, 2, 3, 4
            gross_profit_ratio1 = res_annual_income_url[1]['grossProfitRatio'] # 매출 이익률? 0, 1, 2, 3, 4
            operating_income0 = res_annual_income_url[0]['operatingIncome'] # 영업이익 0, 1, 2, 3, 4
            operating_income1 = res_annual_income_url[1]['operatingIncome'] # 영업이익 0, 1, 2, 3, 4
            # operating_expenses = res_annual_income_url[0]['operatingExpenses'] # 영업 비용 0, 1, 2, 3, 4
            operating_income_ratio0 = res_annual_income_url[0]['operatingIncomeRatio'] # 영업이익률 0, 1, 2, 3, 4
            operating_income_ratio1 = res_annual_income_url[1]['operatingIncomeRatio'] # 영업이익률 0, 1, 2, 3, 4
            net_income0 = res_annual_income_url[0]['netIncome'] # 당기순이익 0, 1, 2, 3, 4
            net_income1 = res_annual_income_url[1]['netIncome'] # 당기순이익 0, 1, 2, 3, 4
            net_income_ratio0 = res_annual_income_url[0]['netIncomeRatio'] # 당기순이익률 0, 1, 2, 3, 4
            net_income_ratio1 = res_annual_income_url[1]['netIncomeRatio'] # 당기순이익률 0, 1, 2, 3, 4
            eps0 = res_annual_income_url[0]['eps'] # 0, 1, 2, 3, 4
            eps1 = res_annual_income_url[1]['eps'] # 0, 1, 2, 3, 4
            total_assets0 = res_url_balance_sheet[0]['totalAssets'] # 0, 1, 2, 3, 4
            total_assets1 = res_url_balance_sheet[1]['totalAssets'] # 0, 1, 2, 3, 4
            total_liabilities0 = res_url_balance_sheet[0]['totalLiabilities'] # 0, 1, 2, 3, 4
            total_liabilities1 = res_url_balance_sheet[1]['totalLiabilities'] # 0, 1, 2, 3, 4
            net_assets0 = float(total_assets0) - float(total_liabilities0)
            net_assets1 = float(total_assets1) - float(total_liabilities1)
            if net_assets0 != 0:
                net_assets_ratio0 = float(net_income0)/net_assets0
            else:
                net_assets_ratio0 = "."
            if net_assets1 != 0:
                net_assets_ratio1 = float(net_income1)/net_assets1
            else:
                net_assets_ratio1 = "."

        else:
            revenue0 = res_annual_income_url[0]['revenue'] # 매출 0, 1, 2, 3, 4
            cost_of_revenue0 = res_annual_income_url[0]['costOfRevenue'] # 매출 원가 0, 1, 2, 3, 4
            gross_profit0 = res_annual_income_url[0]['grossProfit'] # 순매출 0, 1, 2, 3, 4
            gross_profit_ratio0 = res_annual_income_url[0]['grossProfitRatio'] # 매출 이익률? 0, 1, 2, 3, 4
            operating_income0 = res_annual_income_url[0]['operatingIncome'] # 영업이익 0, 1, 2, 3, 4
            # operating_expenses = res_annual_income_url[0]['operatingExpenses'] # 영업 비용 0, 1, 2, 3, 4
            operating_income_ratio0 = res_annual_income_url[0]['operatingIncomeRatio'] # 영업이익률 0, 1, 2, 3, 4
            net_income0 = res_annual_income_url[0]['netIncome'] # 당기순이익 0, 1, 2, 3, 4
            net_income_ratio0 = res_annual_income_url[0]['netIncomeRatio'] # 당기순이익률 0, 1, 2, 3, 4
            eps0 = res_annual_income_url[0]['eps'] # 0, 1, 2, 3, 4
            total_assets0 = res_url_balance_sheet[0]['totalAssets'] # 0, 1, 2, 3, 4
            total_liabilities0 = res_url_balance_sheet[0]['totalLiabilities'] # 0, 1, 2, 3, 4
            net_assets0 = float(total_assets0) - float(total_liabilities0)
            if net_assets0 != 0:
                net_assets_ratio0 = float(net_income0)/net_assets0
            else:
                net_assets_ratio0 = "."


        link1 = res_annual_income_url[0]['link'] # 0, 1, 2, 3, 4
        link2 = res_annual_income_url[0]['finalLink'] # 0, 1, 2, 3, 4

        df1 = pd.DataFrame([
            {
            'symbol': symbol,
            'company_name': company_name,
            'exchange': exchange,
            'country': country,
            'price': price,
            'market_cap': market_cap,
            'stock_count': stock_count,
            'revenue0': revenue0,
            'revenue1': revenue1,
            'revenue2': revenue2,
            'revenue3': revenue3,
            'revenue4': revenue4,
            'cost_of_revenue0': cost_of_revenue0,
            'cost_of_revenue1': cost_of_revenue1,
            'cost_of_revenue2': cost_of_revenue2,
            'cost_of_revenue3': cost_of_revenue3,
            'cost_of_revenue4': cost_of_revenue4,
            'gross_profit0': gross_profit0,
            'gross_profit1': gross_profit1,
            'gross_profit2': gross_profit2,
            'gross_profit3': gross_profit3,
            'gross_profit4': gross_profit4,
            'gross_profit_ratio0': gross_profit_ratio0,
            'gross_profit_ratio1': gross_profit_ratio1,
            'gross_profit_ratio2': gross_profit_ratio2,
            'gross_profit_ratio3': gross_profit_ratio3,
            'gross_profit_ratio4': gross_profit_ratio4,
            'operating_income0': operating_income0,
            'operating_income1': operating_income1,
            'operating_income2': operating_income2,
            'operating_income3': operating_income3,
            'operating_income4': operating_income4,
            'operating_income_ratio0': operating_income_ratio0,
            'operating_income_ratio1': operating_income_ratio1,
            'operating_income_ratio2': operating_income_ratio2,
            'operating_income_ratio3': operating_income_ratio3,
            'operating_income_ratio4': operating_income_ratio4,
            'net_income0': net_income0,
            'net_income1': net_income1,
            'net_income2': net_income2,
            'net_income3': net_income3,
            'net_income4': net_income4,
            'net_income_ratio0': net_income_ratio0,
            'net_income_ratio1': net_income_ratio1,
            'net_income_ratio2': net_income_ratio2,
            'net_income_ratio3': net_income_ratio3,
            'net_income_ratio4': net_income_ratio4,
            'eps0': eps0,
            'eps1': eps1,
            'eps2': eps2,
            'eps3': eps3,
            'eps4': eps4,
            'total_assets0': total_assets0,
            'total_assets1': total_assets1,
            'total_assets2': total_assets2,
            'total_assets3': total_assets3,
            'total_assets4': total_assets4,
            'total_liabilities0': total_liabilities0,
            'total_liabilities1': total_liabilities1,
            'total_liabilities2': total_liabilities2,
            'total_liabilities3': total_liabilities3,
            'total_liabilities4': total_liabilities4,
            'net_assets0': net_assets0,
            'net_assets1': net_assets1,
            'net_assets2': net_assets2,
            'net_assets3': net_assets3,
            'net_assets4': net_assets4,
            'net_assets_ratio0': net_assets_ratio0,
            'net_assets_ratio1': net_assets_ratio1,
            'net_assets_ratio2': net_assets_ratio2,
            'net_assets_ratio3': net_assets_ratio3,
            'net_assets_ratio4': net_assets_ratio4,
            'link1': link1,
            'link2': link2,
            }
        ])

        df = df.append(df1)
    
    except Exception as e:
        print(e)


df.to_excel("finish.xlsx")


