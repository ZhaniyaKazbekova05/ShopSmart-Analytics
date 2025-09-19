# Apache Superset Setup

1. Установи Superset:
   ```bash
   pip install apache-superset
   superset fab create-admin
   superset db upgrade
   superset init
   superset run -p 8088
