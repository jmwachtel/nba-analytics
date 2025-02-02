import sys
import pytz
from datetime import datetime
from sqlalchemy import create_engine

sys.path.append('../../')
from passkeys import RDS_ENDPOINT, RDS_PASSWORD


class BankAccount:
    def __init__(self, connection):
        self.connection = connection
        self.balance = self.load_balance()

    def deposit(self, amount):
        self.balance = self.load_balance()
        self.balance += amount
        self.save_balance()

    def withdraw(self, amount):
        self.balance = self.load_balance()
        self.balance -= amount
        self.save_balance()

    def get_balance(self):
        self.balance = self.load_balance()
        return self.balance

    def set_balance(self, new_balance):
        self.balance = self.load_balance()
        self.balance = new_balance
        self.save_balance()

    def load_balance(self):
        stmt = """SELECT balance FROM bank_account
                  WHERE datetime = (SELECT MAX(datetime) FROM bank_account)
               ;"""

        return self.connection.execute(stmt).fetchone()[0]

    def save_balance(self):
        current_datetime = datetime.now(
            pytz.timezone("America/Denver")).strftime("%Y-%m-%d %H:%M:%S")
        stmt = f"""INSERT INTO bank_account (datetime, balance)
                  VALUES ('{current_datetime}',{float(self.balance)})
                ;"""

        self.connection.execute(stmt)


if __name__ == "__main__":
    username = "postgres"
    password = RDS_PASSWORD
    endpoint = RDS_ENDPOINT
    database = "nba_betting"
    port = "5432"

    engine = create_engine(
        f"postgresql+psycopg2://{username}:{password}@{endpoint}/{database}")

    with engine.connect() as connection:
        bank = BankAccount(connection)
        bank.save_balance()

# Script to create original table in psql command line.
"""CREATE TABLE bank_account (
    datetime timestamp,
    balance float4
);"""
