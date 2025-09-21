import psycopg2

# Подключение к базе
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="ecommerce_olist",
    user="postgres",
    password="kazbekova2005D."
)

cur = conn.cursor()

# Загружаем SQL-запросы из файла
with open("sql/queries.sql", "r") as f:
    queries = f.read().split(";")

for i, query in enumerate(queries, start=1):
    if query.strip():
        cur.execute(query)
        rows = cur.fetchall()
        print(f"\n--- Query {i} results ---")
        for row in rows:
            print(row)

cur.close()
conn.close()
