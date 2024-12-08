import datetime
from api.urls import ApiUrlEnum
from api.request import RequestFMP
from database.db import Database


class StockService:
    """
    Class for stocks service
    """

    def __init__(self):
        self.request = RequestFMP()

    def renew_stocks_list(self):
        url = ApiUrlEnum.STOCK_LIST.value.url
        api_result = self.request.get_api_result(url)
        updated_at = datetime.datetime.now()

        with Database() as db:
            symbols_in_db = db.get_symbols()
            for stock_data in api_result:
                symbol = stock_data['symbol']
                price = stock_data['price']
                name = stock_data['name'] if stock_data['name'] else 'None'
                type_id = stock_data['type']
                exchange_id = stock_data['exchangeShortName']
                if symbol in symbols_in_db:
                    print('update',stock_data)
                    symbols_in_db[symbol] = True
                    db.update_symbol_normal_data(
                        symbol, name, price, type_id, exchange_id, updated_at
                    )
                else:
                    print('insert',stock_data)
                    db.insert_symbol_normal_data(
                        symbol, name, price, type_id, exchange_id, updated_at
                    )
            disappeared_symbols = [symbol for symbol, is_existing in symbols_in_db.items() if not is_existing]
            for symbol in disappeared_symbols:
                db.update_symbol_disappeared_data(symbol, updated_at)
            db.conn.commit()
        print(f"Updated {len(api_result)} stocks")

    def get_income_statements(self, symbol):
        symbol_url = f"{ApiUrlEnum.ANNUAL_INCOME.value.url}/{symbol}"
        params = {'period': 'annual'}
        income_statements = self.request.get_api_result(symbol_url, params)
        return income_statements

    def update_symbol_data(self, symbol):
        income_statements = self.get_income_statements(symbol)
        with Database() as db:
            db.insert_income_statement(income_statements)
            db.update_symbol_is_updated(symbol)
            db.conn.commit()

    def update_all_symbol_datas(self, is_from_first = True):
        """
        Insert income statements for all symbols
        using method update_symbol_data
        """
        with Database() as db:
            symbols_to_be_updated = db.get_symbols_to_be_updated(is_from_first)
            for symbol in symbols_to_be_updated:
                self.update_symbol_data(symbol)

if __name__ == "__main__":
    import sys

    service = StockService()
    
    if len(sys.argv) < 2:
        print("Error: Command is not executed. Please specify a method.")
        exit(1)

    method_name = sys.argv[1]
    method = getattr(service, method_name, None)
    args = sys.argv[2:]  # Get additional arguments
    if method is not None and callable(method):
        if len(args) > 0:
            method(*args)  # Pass the arguments to the method
        else:
            method()
    else:
        print(f"Error: Method {method_name} not found")
