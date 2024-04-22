FROM python:3.8

COPY *.py /app/
COPY labeled.csv /app/
COPY requirements.txt /app/

WORKDIR /app/

RUN pip install -r requirements.txt

RUN python -c "import nltk; nltk.download('stopwords')"
RUN python -c "import nltk; nltk.download('punkt')"

CMD ["python", "train.py"]

EXPOSE 80
