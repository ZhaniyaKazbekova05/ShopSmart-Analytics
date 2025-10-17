# scripts/stream_simulator.py
import time
import random
import psycopg2
from datetime import datetime, timedelta

DB = dict(host="localhost", port=5432, dbname="ecommerce_olist", user="postgres", password="kazbekova2005D.")

PAYMENT_TYPES = ["credit_card", "boleto", "voucher", "debit_card"]

def main():
    conn = psycopg2.connect(**DB)
    conn.autocommit = True
    cur = conn.cursor()

    while True:
        # берём любой существующий order_id (чтобы не нарушать FK)
        cur.execute("SELECT order_id FROM orders ORDER BY random() LIMIT 1;")
        order_id = cur.fetchone()[0]

        ptype = random.choice(PAYMENT_TYPES)
        value = round(random.uniform(20, 300), 2)
        

        # вставляем платеж
        cur.execute("""
            INSERT INTO order_payments (order_id, payment_type, payment_value)
            VALUES (%s, %s, %s);
        """, (order_id, ptype, value))

        # иногда добавляем новый item к этому заказу
        cur.execute("SELECT product_id FROM products ORDER BY random() LIMIT 1;")
        product_id = cur.fetchone()[0]
        cur.execute("""
            WITH last AS (
              SELECT COALESCE(MAX(order_item_id), 0) AS m FROM order_items WHERE order_id = %s
            )
            INSERT INTO order_items (order_id, order_item_id, product_id, seller_id, shipping_limit_date, price, freight_value)
            SELECT %s, m+1, %s,
                   (SELECT seller_id FROM sellers ORDER BY random() LIMIT 1),
                   NOW() + INTERVAL '3 day',
                   %s, %s
            FROM last;
        """, (order_id, order_id, product_id, round(random.uniform(10,200),2), round(random.uniform(2,30),2)))

        print(f"[{datetime.now().strftime('%H:%M:%S')}] +1 payment ({ptype}, {value}) для order {order_id}")
        time.sleep(10)  # меняй на 5–20 сек по желанию

if __name__ == "__main__":
    main()
# --- Разрешить загрузку CSV ---
UPLOAD_FOLDER = "/Users/zhaniyakazbekova/Desktop"
ALLOWED_EXTENSIONS = {"csv", "tsv", "txt"}
FEATURE_FLAGS = {
    "ALLOW_FILE_UPLOAD": True
}
