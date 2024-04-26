FROM python:3.8

COPY *.py /app/
COPY labeled.csv /app/
COPY requirements.txt /app/
COPY base_model_pipeline.joblib /app/base_model_pipeline.joblib


WORKDIR /app/

RUN pip install -r requirements.txt

RUN python -c "import nltk; nltk.download('stopwords')"
RUN python -c "import nltk; nltk.download('punkt')"

EXPOSE 80


CMD ["uvicorn", "server:app", "--reload", "--host", "0.0.0.0", "--port", "80"]