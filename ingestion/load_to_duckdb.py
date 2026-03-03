import duckdb
import os

# Define project base path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_PATH = os.path.join(BASE_DIR, "raw_zone")
DB_PATH = os.path.join(BASE_DIR, "warehouse.duckdb")

# Connect to DuckDB database
con = duckdb.connect(DB_PATH)

# Create schema
con.execute("CREATE SCHEMA IF NOT EXISTS raw_layer;")

# Drop tables if they exist (idempotency)
con.execute("DROP TABLE IF EXISTS raw_layer.users;")
con.execute("DROP TABLE IF EXISTS raw_layer.products;")
con.execute("DROP TABLE IF EXISTS raw_layer.orders;")

# Load CSVs into tables
con.execute(f"""
CREATE TABLE raw_layer.users AS
SELECT * FROM read_csv_auto('{RAW_PATH}/users.csv');
""")

con.execute(f"""
CREATE TABLE raw_layer.products AS
SELECT * FROM read_csv_auto('{RAW_PATH}/products.csv');
""")

con.execute(f"""
CREATE TABLE raw_layer.orders AS
SELECT * FROM read_csv_auto('{RAW_PATH}/orders.csv');
""")

print("Raw tables successfully loaded into DuckDB.")

con.close()