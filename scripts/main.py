import psycopg2
import pandas as pd

# подключение к базе
conn = psycopg2.connect(
    dbname="ecommerce_olist",
    user="postgres",
    password="1234",  # замени на свой пароль
    host="localhost",
    port="5432"
)

# запрос для примера
query = """
SELECT p.product_category_name, SUM(oi.price + oi.freight_value) AS revenue
FROM order_items oi
JOIN products p USING (product_id)
GROUP BY p.product_category_name
ORDER BY revenue DESC
LIMIT 10;
"""

df = pd.read_sql_query(query, conn)
print(df)

# сохранить результат в CSV
df.to_csv("top_categories.csv", index=False)

conn.close()
