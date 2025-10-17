import psycopg2
import pandas as pd

# --- Подключение к PostgreSQL ---
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="ecommerce_olist",
    user="postgres",
    password="kazbekova2005D."
)
cur = conn.cursor()

# --- Загружаем CSV ---
csv_path = "/Users/zhaniyakazbekova/Desktop/order_payments.csv"
df = pd.read_csv(csv_path)

# --- Имя новой таблицы ---
table_name = "order_payments_csv"

# --- Пересоздаём таблицу ---
cur.execute(f"DROP TABLE IF EXISTS {table_name};")
cur.execute(f"""
CREATE TABLE {table_name} (
    order_id TEXT,
    payment_sequential TEXT,
    payment_type TEXT,
    payment_installments TEXT,
    payment_value NUMERIC
);
""")

# --- Вставляем строки ---
for _, row in df.iterrows():
    cur.execute(f"""
        INSERT INTO {table_name} (order_id, payment_sequential, payment_type, payment_installments, payment_value)
        VALUES (%s, %s, %s, %s, %s);
    """, tuple(row))

conn.commit()
cur.close()
conn.close()

print(f"✅ CSV успешно импортирован в таблицу {table_name}")
