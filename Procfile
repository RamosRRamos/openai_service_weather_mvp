web: gunicorn openai_service.wsgi --log-file -
worker: celery -A openai_service worker --loglevel=info
