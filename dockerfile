FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

WORKDIR /app/

COPY ./requirements.txt /app/requirements.txt
COPY ./sample.env .env

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

ENV PYTHONPATH=/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]