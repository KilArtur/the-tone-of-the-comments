FROM python:3.8-slim-buster

COPY *.py /app/
COPY labeled.csv /app/
COPY requirements.txt /app/
COPY base_model_pipeline.joblib /app/base_model_pipeline.joblib

WORKDIR /app/

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

RUN python train.py

EXPOSE 80

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80", "--reload"]