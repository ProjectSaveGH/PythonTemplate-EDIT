import sqlite3
from sqlite3 import Connection
from lib.logger.logger import Logger
from lib.moduleExtension.eval import contains_sql

l: Logger = Logger(printLog=True)

def create_connection(db_file: str) -> Connection | None:
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        l.info(f"Connected to database: {db_file}")
    except sqlite3.Error as e:
        l.error(f"Error connecting to database: {e}")
    return conn

def create_table(conn: Connection, create_table_sql: str) -> None:
    """Create a table from the create_table_sql statement."""
    if contains_sql(create_table_sql):
        l.error("SQL statement contains dangerous keywords")
        return
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        l.info("Table created successfully")
    except sqlite3.Error as e:
        l.error(f"Error creating table: {e}")

def execute_query(conn: Connection, query: str, params: tuple = ()) -> None:
    """Execute a single query."""
    if contains_sql(query):
        l.error("SQL statement contains dangerous keywords")
        return
    try:
        c = conn.cursor()
        c.execute(query, params)
        conn.commit()
        l.info("Query executed successfully")
    except sqlite3.Error as e:
        l.error(f"Error executing query: {e}")

def fetch_all(conn: Connection, query: str, params: tuple = ()) -> list:
    """Fetch all results from a query."""
    if contains_sql(query):
        l.error("SQL statement contains dangerous keywords")
        return []
    try:
        c = conn.cursor()
        c.execute(query, params)
        rows = c.fetchall()
        l.info("Query fetched successfully")
        return rows
    except sqlite3.Error as e:
        l.error(f"Error fetching query: {e}")
        return []

def delete_table(conn: Connection, table_name: str) -> None:
    """Delete a table."""
    query = f"DROP TABLE IF EXISTS {table_name}"
    if contains_sql(query):
        l.error("SQL statement contains dangerous keywords")
        return
    try:
        c = conn.cursor()
        c.execute(query)
        conn.commit()
        l.info(f"Table {table_name} deleted successfully")
    except sqlite3.Error as e:
        l.error(f"Error deleting table: {e}")

def close_connection(conn: Connection) -> None:
    """Close the database connection."""
    if conn:
        conn.close()
        l.info("Database connection closed")