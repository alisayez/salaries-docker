FROM python:3.8

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

EXPOSE 8501

WORKDIR /python

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]