import os

from superset.config import *  # импорт
SECRET_KEY = "hduMO2aNVOrAQbc3yuwoFt6g/TM5cBTnh5TSp7bvzEYNsT61n8aIklRE"
 
# 💾 Путь к базе метаданных Superset
SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/zhaniyakazbekova/superset-env/superset.db'

# 🌐 Включаем доступ
SUPERSET_WEBSERVER_PORT = 8088

ENABLE_CORS = True
CORS_OPTIONS = {
    "supports_credentials": True,
    "origins": ["*"],
    "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    "allow_headers": ["*"],
}


