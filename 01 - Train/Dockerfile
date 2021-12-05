FROM python:3.8.8

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

WORKDIR /python

ENTRYPOINT ["python","/python/train.py"]

