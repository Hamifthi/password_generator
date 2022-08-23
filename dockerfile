FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

WORKDIR /app/

COPY ./requirements.txt /app/requirements.txt
COPY ./sample.env .env

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

ENV PYTHONPATH=/app

COPY ["./entrypoint.sh", "/"]

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
