import pandas as pd
import nltk
import joblib
import string
from nltk.corpus import stopwords as nltk_stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from pymystem3 import Mystem

def prep_text(sentence: str):
    """
    Функция выполняет предобработку текста на русском языке,
    включая удаление пунктуации и стоп-слов, лемматизацию слов
    """
    tokens = word_tokenize(sentence, language="russian")
    tokens = [i for i in tokens if i not in string.punctuation]
    tokens = [i for i in tokens if i.lower() not in russian_stop_words]
    tokens = [m.lemmatize(i)[0] for i in tokens]
    return tokens



if __name__ == '__main__':
    way = 'labeled.csv'
    try:
        df = pd.read_csv(way)
        nltk.download('stopwords')
        nltk.download('punkt')
    except Exception as e:
        print(f'Ошибка {e}')

    nltk.download('stopwords')


    print('Данные подгружены')

    russian_stop_words = nltk_stopwords.words('russian')
    m = Mystem()

    base_model_pipeline = Pipeline([
        ("vectorizer", TfidfVectorizer(tokenizer= prep_text)),
        ("model", LogisticRegression(C=1,
                                     penalty='l2',
                                     class_weight='balanced',
                                     random_state=12345))
    ]
    )

    print('Создался пайплайн')

    # обучение пайплайна
    base_model_pipeline.fit(df["comment"][:10], df["toxic"][:10])
    joblib.dump(base_model_pipeline, "./base_model_pipeline.joblib")

    print('Пайплайн обучился и успешно сохранен')