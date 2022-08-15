import pandas as pd
import requests


BASE_URL = "https://financialmodelingprep.com/"

API_KEY = "sddd"

SYMBOL_LIST_URL = 'https://financialmodelingprep.com/api/v3/financial-statement-symbol-lists?apikey='
ANNUAL_INCOME_URL = "https://financialmodelingprep.com/api/v3/income-statement/{}?apikey="
URL_COMPANIES_PROFILE = "https://financialmodelingprep.com/api/v3/profile/{}?apikey="
URL_BALANCE_SHEET = 'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{}?apikey='
URL_MARKET_CAPITALIZATION = 'https://financialmodelingprep.com/api/v3/market-capitalization/{}?apikey='
FINANCIAL_RATIO_URL = 'https://financialmodelingprep.com/api/v3/ratios-ttm/{}?apikey='

symbol_list_url = SYMBOL_LIST_URL + API_KEY
req_symbol_list = requests.get(symbol_list_url)
res_symbol_list = req_symbol_list.json()

fail_list = []

df = pd.DataFrame()

for i in res_symbol_list:
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
        
        financial_ratio_url = FINANCIAL_RATIO_URL.format(i) + API_KEY
        req_financial_ratio = requests.get(financial_ratio_url)
        res_financial_ratio = req_financial_ratio.json()


        symbol = res_annual_income_url[0]['symbol']
        company_name = res_companies_profile[0]['companyName']
        exchange = res_companies_profile[0]['exchangeShortName']
        country = res_companies_profile[0]['country']
        price = res_companies_profile[0]['price']
        market_cap = res_url_market_capitalization[0]['marketCap']
        stock_count = float(market_cap)/float(price)
        
        peRatioTTM = res_financial_ratio[0]['peRatioTTM']
        pegRatioTTM = res_financial_ratio[0]['pegRatioTTM']
        pbrTTM = res_financial_ratio[0]['priceBookValueRatioTTM']
        debtRatioTTM = res_financial_ratio[0]['debtRatioTTM']
        
        revenue0 = res_annual_income_url[0]['revenue'] # 매출 0, 1, 2, 3, 4
        if res_annual_income_url[1]['revenue']:
            revenue1 = res_annual_income_url[1]['revenue'] # 매출 0, 1, 2, 3, 4
        else: 
            revenue1 = 0
        if res_annual_income_url[2]['revenue']:
            revenue2 = res_annual_income_url[2]['revenue']
        else:
            revenue2 = 0
        if res_annual_income_url[3]['revenue']:
            revenue3 = res_annual_income_url[3]['revenue']
        else:
            revenue3 = 0
        if res_annual_income_url[4]['revenue']:
            revenue4 = res_annual_income_url[4]['revenue']
        
        
        operating_income0 = res_annual_income_url[0]['operatingIncome']
        if res_annual_income_url[1]['operatingIncome']:
            operating_income1 = res_annual_income_url[1]['operatingIncome']
        else:
            operating_income1 = 0
        if res_annual_income_url[2]['operatingIncome']:
            operating_income2 = res_annual_income_url[2]['operatingIncome']
        else:
            operating_income2 = 0
            
        if res_annual_income_url[3]['operatingIncome']:
            operating_income3 = res_annual_income_url[3]['operatingIncome']
        else:
            operating_income3 = 0
        if res_annual_income_url[4]['operatingIncome']:
            operating_income4 = res_annual_income_url[4]['operatingIncome']
        else:
            operating_income4 = 0
        
        operating_income_ratio0 = res_annual_income_url[0]['operatingIncomeRatio']
        if res_annual_income_url[1]['operatingIncomeRatio']:
            operating_income_ratio1 = res_annual_income_url[1]['operatingIncomeRatio']
        else:
            operating_income_ratio1 = 0
        if res_annual_income_url[2]['operatingIncomeRatio']:
            operating_income_ratio2 = res_annual_income_url[2]['operatingIncomeRatio']
        else:
            operating_income_ratio2 = 0
        if res_annual_income_url[3]['operatingIncomeRatio']:    
            operating_income_ratio3 = res_annual_income_url[3]['operatingIncomeRatio']
        else: 
            operating_income_ratio3 = 0
        if res_annual_income_url[4]['operatingIncomeRatio']:
            operating_income_ratio4 = res_annual_income_url[4]['operatingIncomeRatio']
        else:
            operating_income_ratio4 = 0

        net_income0 = res_annual_income_url[0]['netIncome']
        net_income_ratio0 = res_annual_income_url[0]['netIncomeRatio']
        if res_annual_income_url[1]['netIncome']:
            net_income1 = res_annual_income_url[1]['netIncome']
            net_income_ratio1 = res_annual_income_url[1]['netIncomeRatio']
        else:
            net_income1 = 0
            net_income_ratio1 = 0
        if res_annual_income_url[2]['netIncome']:
            net_income2 = res_annual_income_url[2]['netIncome']
            net_income_ratio2 = res_annual_income_url[2]['netIncomeRatio']
        else:
            net_income2 = 0
            net_income_ratio2 = 0
        if res_annual_income_url[3]['netIncome']:
            net_income3 = res_annual_income_url[3]['netIncome']
            net_income_ratio3 = res_annual_income_url[3]['netIncomeRatio']
        else:
            net_income3 = 0
            net_income_ratio3 = 0
        if res_annual_income_url[4]['netIncome']:
            net_income4 = res_annual_income_url[4]['netIncome']
            net_income_ratio4 = res_annual_income_url[4]['netIncomeRatio']
        else:
            net_income4 = 0
            net_income_ratio4 = 0
        
        eps0 = res_annual_income_url[0]['eps']
        if res_annual_income_url[1]['eps']:
            eps1 = res_annual_income_url[1]['eps']
        else:
            eps1 = 0
        if res_annual_income_url[2]['eps']:
            eps2 = res_annual_income_url[2]['eps']
        else:
            eps2 = 0
        if res_annual_income_url[3]['eps']:
            eps3 = res_annual_income_url[3]['eps']
        else:
            eps3 = 0
        if res_annual_income_url[4]['eps']:
            eps4 = res_annual_income_url[4]['eps']
        else:
            eps4 = 0
        
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
            'p/e_ratio': peRatioTTM,
            'peg_ratio': pegRatioTTM,
            'pbr': pbrTTM,
            'debt_ratio': debtRatioTTM,
            'revenue0': revenue0,
            'revenue1': revenue1,
            'revenue2': revenue2,
            'revenue3': revenue3,
            'revenue4': revenue4,
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
            'link1': link1,
            'link2': link2,
            }
        ])

        df = df.append(df1)
    
    except Exception as e:
        print("-----")
        print(e)
        print("-----")
        print(i)
        print("-----")
        dict = [i, e]
        fail_list.append(dict)


df.to_excel("selected_list.xlsx")
pd.DataFrame(fail_list, columns=['symbol', 'reason']).to_excel("fail_list.xlsx")