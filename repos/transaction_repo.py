import sys
sys.path.append("data/")
from data.db_util import query, query_select

def save_transaction(customer_name, total_amount):
    query(f"INSERT INTO transactions (customer_name, total_amount) VALUES ('{customer_name}', {total_amount})")

def get_transaction(customer_name):
    db_list = query_select(f"SELECT * FROM transactions WHERE customer_name = '{customer_name}'")
    return db_list