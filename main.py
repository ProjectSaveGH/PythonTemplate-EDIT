from lib.database.database import *

conn = create_connection("test.db")
create_table(conn, "CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
execute_query(conn, "INSERT INTO test (name) VALUES (?)", ("test",))
print(fetch_all(conn, "SELECT * FROM test"))
delete_table(conn, "test")
close_connection(conn)