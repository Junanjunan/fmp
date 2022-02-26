import financedatabase as fd

# cate = fd.select_equities(country='United States', industry='Resorts & Casinos')
cate = fd.select_equities(country='United States')
# print(cate['AAPL'])

from yfinance.utils import get_json
from yfinance import download

fundamentals = {}
for symbol in list(cate)[0:3]:
    print(symbol)
    fundamentals[symbol] = get_json("https://finance.yahoo.com/quote/" + symbol)

print(2)
# stocks = download(list(cate))
print(3)

import pandas as pd

df = pd.DataFrame()

for k in fundamentals:
    if len(fundamentals[k]) == 0:
        print("{} is empty".format(k))
        pass
    else:
        print(4)
        temp = pd.DataFrame(
            [
                {
                    "ticker": fundamentals[k]['symbol'],
                    "name":fundamentals[k]['quoteType']['longName'],
                    "quickRatio":fundamentals[k]['financialData']['quickRatio'],
                    "totalRevenue":fundamentals[k]['financialData']["totalRevenue"],
                    "test": fundamentals
        }
        ]
        )
        print(5)
        df = pd.concat([df, temp],0)
        print(6)
        print(k)

df.to_excel('new.xlsx')

import plotly.express as px

px.bar(data_frame = df, y="quickRatio", x="name").update_xaxes(categoryorder="total descending")
