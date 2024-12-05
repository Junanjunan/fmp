import psycopg2
from pathlib import Path
from settings import db_name, db_user, db_password, db_host, db_port
from api_enums import SymbolTypeEnum, ExchangeEnum
from psycopg2.extras import execute_values


class Database:
    def __init__(self):
        # Database connection parameters from environment variables
        self.db_params = {
            'dbname': db_name,
            'user': db_user,
            'password': db_password,
            'host': db_host,
            'port': db_port
        }
        self.conn = None
        self.cur = None

    def __enter__(self):
        """Context manager entry"""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.close()

    def connect(self):
        """Establish database connection"""
        try:
            self.conn = psycopg2.connect(**self.db_params)
            self.cur = self.conn.cursor()
        except Exception as e:
            print(f"Error connecting to database: {str(e)}")
            raise

    def close(self):
        """Close database connection"""
        if self.cur:
            self.cur.close()
            self.cur = None
        if self.conn:
            self.conn.close()
            self.conn = None

    def create_table(self, sql_file_name):
        """Create tables from SQL file"""
        try:
            sql_file_path = Path(__file__).parent / 'sql' / sql_file_name
            with open(sql_file_path, 'r') as file:
                sql_script = file.read()
            self.cur.execute(sql_script)
            self.conn.commit()
            print(f"Table {sql_file_name} created successfully")
        except Exception as e:
            print(f"Error creating table: {str(e)}")
            raise

    def fill_types_table(self):
        symbol_type_list = SymbolTypeEnum.get_symbol_type_list()
        execute_values(
            self.cur,
            "INSERT INTO types (id) VALUES %s",
            [(symbol,) for symbol in symbol_type_list]
        )
        self.conn.commit()
        print("Types table filled successfully")

    def fill_exchanges_table(self):
        exchange_dict = ExchangeEnum.get_exchange_dict()
        execute_values(
            self.cur,
            "INSERT INTO exchanges (id, name) VALUES %s",
            [(id, name) for id, name in exchange_dict.items()]
        )
        self.conn.commit()
        print("Exchanges table filled successfully")

    def get_symbols(self):
        """
        Get symbols from the database
        Returns a dictionary with symbols as keys and False as values
        False means that the symbol is not existing in the API result.
        If the symbol is existing in the API result, the value is set to True.
        """
        self.cur.execute("SELECT id FROM symbols")
        symbols_in_db = {row[0]: False for row in self.cur.fetchall()}
        return symbols_in_db

    def update_symbol_normal_data(self, symbol, name, price, type_id, exchange_id, updated_at):
        self.cur.execute(
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
    
    def insert_symbol_normal_data(self, symbol, name, price, type_id, exchange_id, updated_at):
        self.cur.execute(
            """
            INSERT INTO symbols
                (id, name, price, type_id, exchange_id, is_existing, updated_at)
            VALUES (%s, %s, %s, %s, %s, TRUE, %s)
            """,
            (symbol, name, price, type_id, exchange_id, updated_at)
        )

    def update_symbol_disappeared_data(self, symbol, updated_at):
        # Set is_existing to FALSE about disappeared symbols
        self.cur.execute(
            """
            UPDATE symbols SET is_existing = FALSE, updated_at = %s WHERE id = %s
            """,
            (updated_at, symbol)
        )

if __name__ == "__main__":
    import sys
    
    with Database() as db:
        if len(sys.argv) < 2:
            print("Error: Command is not executed. Please specify a method.")
            exit(1)

        method_name = sys.argv[1]
        method = getattr(db, method_name, None)
        args = sys.argv[2:]  # Get additional arguments
        if method is not None and callable(method):
            method(*args)  # Pass the arguments to the method
        else:
            print(f"Error: Method {method_name} not found")
