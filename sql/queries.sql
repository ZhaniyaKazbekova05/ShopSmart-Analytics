-- 1. Выручка по категориям
SELECT p.product_category_name, SUM(oi.price + oi.freight_value) AS revenue
FROM order_items oi
JOIN products p USING (product_id)
GROUP BY p.product_category_name
ORDER BY revenue DESC
LIMIT 10;

-- 2. Средний чек по штатам
WITH t AS (
  SELECT o.order_id, SUM(oi.price + oi.freight_value) AS order_total
  FROM orders o JOIN order_items oi USING (order_id)
  GROUP BY o.order_id
)
SELECT c.customer_state, ROUND(AVG(t.order_total),2) AS avg_order_value
FROM t
JOIN orders o ON o.order_id = t.order_id
JOIN customers c ON c.customer_id = o.customer_id
GROUP BY c.customer_state
ORDER BY avg_order_value DESC;

-- 3. Количество заказов по месяцам
SELECT date_trunc('month', order_purchase_timestamp) AS month, COUNT(*) AS orders_count
FROM orders
GROUP BY 1
ORDER BY 1;

-- 4. Распределение статусов заказов
SELECT order_status, COUNT(*) AS count
FROM orders
GROUP BY order_status;

-- 5. Топ-10 продавцов по выручке
SELECT s.seller_id, SUM(oi.price + oi.freight_value) AS revenue
FROM order_items oi
JOIN sellers s USING (seller_id)
GROUP BY s.seller_id
ORDER BY revenue DESC
LIMIT 10;

-- 6. Среднее время доставки
SELECT AVG(order_delivered_customer_date - order_purchase_timestamp) AS avg_delivery_time
FROM orders
WHERE order_delivered_customer_date IS NOT NULL;

-- 7. Проблемные заказы
SELECT order_status, COUNT(*) AS cnt
FROM orders
WHERE order_status IN ('canceled','unavailable')
GROUP BY order_status;

-- 8. Средняя оценка по категориям
SELECT p.product_category_name, ROUND(AVG(r.review_score),2) AS avg_score
FROM order_reviews r
JOIN orders o USING (order_id)
JOIN order_items oi ON oi.order_id = o.order_id
JOIN products p ON p.product_id = oi.product_id
GROUP BY p.product_category_name
ORDER BY avg_score DESC
LIMIT 10;

-- 9. Динамика выручки по месяцам
SELECT date_trunc('month', o.order_purchase_timestamp) AS month,
       SUM(oi.price + oi.freight_value) AS revenue
FROM orders o
JOIN order_items oi USING (order_id)
GROUP BY 1
ORDER BY 1;

-- 10. ТОП-10 городов покупателей
SELECT c.customer_city, COUNT(*) AS orders_count
FROM orders o
JOIN customers c USING (customer_id)
GROUP BY c.customer_city
ORDER BY orders_count DESC
LIMIT 10;
