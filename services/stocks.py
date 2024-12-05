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
        try:
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
                        symbols_in_db[symbol] = True
                        # Execute update query
                        db.cur.execute(
                            """
                            UPDATE symbols SET
                                name = %s,
                                price = %s,
                                type_id = %s,
                                exchange_id = %s,
                                is_existing = TRUE,
                                updated_at = %s
                            WHERE id = %s
                            """,
                            (name, price, type_id, exchange_id, updated_at, symbol)
                        )
                    else:
                        # Execute insert query
                        print(stock_data)
                        db.cur.execute(
                            """
                            INSERT INTO symbols
                                (id, name, price, type_id, exchange_id, is_existing, updated_at)
                            VALUES (%s, %s, %s, %s, %s, TRUE, %s)
                            """,
                            (symbol, name, price, type_id, exchange_id, updated_at)
                        )
                disappeared_symbols = [symbol for symbol, is_existing in symbols_in_db.items() if not is_existing]
                for symbol in disappeared_symbols:
                    # Set is_existing to FALSE about disappeared symbols
                    db.cur.execute(
                        """
                        UPDATE symbols SET is_existing = FALSE, updated_at = %s WHERE id = %s
                        """,
                        (updated_at, symbol)
                    )
                db.conn.commit()
            print(f"Updated {len(api_result)} stocks")
        except Exception as e:
            db.conn.rollback()
            print(f"Error: {e}")


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
