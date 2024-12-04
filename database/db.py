import psycopg2
from settings import db_name, db_user, db_password, db_host, db_port


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