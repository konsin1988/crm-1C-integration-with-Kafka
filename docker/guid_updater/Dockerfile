FROM python:3.11-slim

WORKDIR /app

COPY ./guid_updater /app
COPY ./docker/guid_updater/requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
