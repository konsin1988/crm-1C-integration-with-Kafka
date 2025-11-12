FROM python:3.11-slim

WORKDIR /app

COPY ./app /app
COPY ./docker/account_creation/requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

CMD ["fastapi", "run", "/app/main.py", "--port", "8000"]
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]



