import psycopg2
import pandas as pd

# подключение к базе
conn = psycopg2.connect(
    host="localhost",
    dbname="ecommerce_olist",
    user="postgres",
    password="kazbekova2005D.",
    port=5432
)

# загружаем данные
df = pd.read_sql("SELECT * FROM order_payments;", conn)

# сохраняем в CSV
df.to_csv("/Users/zhaniyakazbekova/Desktop/order_payments.csv", index=False)

print("✅ CSV saved on Desktop!")
conn.close()
