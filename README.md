Пример запуска фреймворка с помощью uWSGI:
uwsgi --http :8000 --wsgi-file app.py
Пример запуска фреймворка с помощью Gunicorn:
gunicorn app:application