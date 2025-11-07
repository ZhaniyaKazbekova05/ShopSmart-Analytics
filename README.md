ShopSmart Analytics — E-commerce Data & Monitoring System
🌟 Overview

ShopSmart Analytics — это умная аналитическая и мониторинговая система для интернет-магазина,
которая помогает бизнесу понимать клиентов, отслеживать заказы и контролировать стабильность работы платформы.

Проект сочетает аналитику данных и систему мониторинга, чтобы принимать решения на основе фактов,
а не догадок.

🎯 Key Features
📊 1. Data Analytics

Аналитическая часть проекта включает:

SQL-запросы для анализа клиентов, заказов и продаж

автоматическую генерацию визуализаций

экспорт отчётов в Excel и интерактивные графики

Примеры аналитики:

Средний чек и частота покупок

ТОП-10 категорий по выручке

Динамика заказов по месяцам

ТОП-5 городов по продажам

🧠 2. Real-Time Monitoring (Prometheus + Grafana)

Мониторинг позволяет наблюдать:

состояние и производительность базы данных

внутренние метрики системы (нагрузка, задержки, ошибки)

пользовательские показатели (погода, курс валют и др.)

📌 Используемые экспортеры:
Экспортер	Описание	Пример метрик
Database Exporter	собирает данные о состоянии PostgreSQL	pg_up, pg_locks_count, pg_database_size_bytes
Custom Exporter (Python)	публикует бизнес- и системные метрики	weather_temperature, usd_kzt_rate, system_random_load
🔔 Smart Alerts

Система автоматически уведомляет при возникновении проблем:

Alert	Условие	Значение
🔴 Database Down	pg_up == 0	Потеря соединения с базой
🟠 High Lock Count	sum(pg_locks_count) > 5	Возможная блокировка запросов
🌡️ High Temperature	weather_temperature > 35	Перегрев (симулированная метрика)
💵 Exchange Rate Drop	usd_kzt_rate < 440	Падение курса валюты
⚙️ System Overload	system_random_load > 80	Системная нагрузка превышает норму
📈 Dashboards

Визуализация в Grafana включает два дашборда:

Dashboard	Назначение	Файл
Database Dashboard	Состояние PostgreSQL и запросов	postgres_dashboard.json
Custom Exporter Dashboard	Температура, влажность, курс валют, нагрузка	custom_exporter_dashboard.json

Пример отображения:

📦 База данных: состояние, блокировки, размер

🌤️ Температура и влажность (по городам)

💰 Валютный курс USD/KZT

⚙️ Системная нагрузка в реальном времени

🧩 Tech Stack
Технология	Назначение
PostgreSQL	Хранение данных
Python (pandas, prometheus_client)	Аналитика и Custom Exporter
Prometheus	Сбор и хранение метрик
Grafana	Визуализация и уведомления
Apache Superset	Бизнес-аналитика
VS Code / GitHub	Разработка и управление проектом
🚀 How It Works (in 3 Steps)

1️⃣ Data Collection → PostgreSQL хранит заказы, клиентов и товары
2️⃣ Monitoring → Prometheus собирает метрики с Exporter-ов
3️⃣ Visualization → Grafana отображает метрики и отправляет алерты
