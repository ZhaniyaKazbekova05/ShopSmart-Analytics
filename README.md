# ShopSmart Analytics – E-commerce Project

**Company (fictional):** ShopSmart – онлайн-маркетплейс в Бразилии.  
**Analyst:** Raihan Kasymkyzy

## 📌 Project Overview
Учебный проект по анализу e-commerce датасета [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).  

Цели:
- Построить схему базы данных (PostgreSQL).
- Импортировать данные и выполнить SQL-запросы.
- Подготовить Python-скрипт для аналитики.
- Визуализировать результаты в Apache Superset.

## 📂 Structure
- `sql/schema_postgres.sql` — SQL для создания таблиц.
- `sql/queries.sql` — 10 аналитических SQL-запросов.
- `scripts/main.py` — Python-скрипт.
- `docs/erd_dbdiagram.txt` — ER-диаграмма базы.
- `docs/superset_setup.md` — инструкция по настройке Superset.
- `img/superset_dashboard.png` — скриншот из Superset.

## 🚀 How to Run
1. Установи PostgreSQL и создай базу:
   ```sql
   CREATE DATABASE ecommerce_olist;
