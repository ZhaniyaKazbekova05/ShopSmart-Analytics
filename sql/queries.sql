-- Общее количество уникальных клиентов
SELECT COUNT(*) AS total_customers
FROM customers;
-- Общее количество заказов
SELECT COUNT(*) AS total_orders
FROM orders;
-- Средняя сумма платежа за заказ
SELECT AVG(payment_value) AS avg_order_value
FROM order_payments;
-- Категории товаров с наибольшей выручкой
SELECT p.product_category_name,
       SUM(oi.price + oi.freight_value) AS total_revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_category_name
ORDER BY total_revenue DESC
LIMIT 10;
-- Сколько заказов в каждом статусе
SELECT order_status, COUNT(*) AS total
FROM orders
GROUP BY order_status
ORDER BY total DESC;

-- Среднее количество дней от покупки до доставки
SELECT AVG(order_delivered_customer_date - order_purchase_timestamp) AS avg_delivery_time
FROM orders
WHERE order_delivered_customer_date IS NOT NULL;
-- Города с наибольшим числом клиентов
SELECT customer_city, COUNT(*) AS total_customers
FROM customers
GROUP BY customer_city
ORDER BY total_customers DESC
LIMIT 5;
-- Средний рейтинг по отзывам
SELECT AVG(review_score) AS avg_review_score
FROM order_reviews;
-- Общее количество уникальных продавцов
SELECT COUNT(*) AS total_sellers
FROM sellers;

-- Популярные способы оплаты
SELECT payment_type, COUNT(*) AS total
FROM order_payments
GROUP BY payment_type
ORDER BY total DESC
LIMIT 5;


-- Список клиентов и количество заказов у каждого (включая тех, у кого заказов нет)
SELECT c.customer_id,
       COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
ORDER BY total_orders DESC
LIMIT 10;

-- Список продавцов и количество товаров, которые они продали
SELECT s.seller_id,
       COUNT(oi.product_id) AS total_products_sold
FROM order_items oi
RIGHT JOIN sellers s ON oi.seller_id = s.seller_id
GROUP BY s.seller_id
ORDER BY total_products_sold DESC
LIMIT 10;
