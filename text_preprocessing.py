import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords as nltk_stopwords
from pymystem3 import Mystem

russian_stop_words = nltk_stopwords.words('russian')
m = Mystem()

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