import sqlite3
import pandas as pd

conn = sqlite3.connect('Chinook_Sqlite.sqlite')

query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = pd.read_sql_query(query, conn)

dfs ={}
for table_name in tables['name']:
    dfs[table_name] = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    
query_join = """
SELECT c.*, e.*
FROM Customer c
INNER JOIN Employee e ON c.SupportRepId = e.EmployeeId
"""

df_sql = pd.read_sql_query(query_join, conn)
csv_path = "query.csv"
df_sql.to_csv(csv_path, index=False)
print(f"\nArquivo CSV gerado com sucesso: {csv_path}")
print(f"Total de linhas exportadas: {len(df_sql)}")

conn.close()

# merge_join = dfs['Customer'].merge(
#     dfs['Employee'],
#     left_on='SupportRepId',
#     right_on='EmployeeId',
#     how='inner',
#     suffixes=('_cliente', '_funcionario')
# )

