import nltk
from nltk.corpus import stopwords
from string import punctuation
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

words_to_avoid = set(stopwords.words("english") + list(punctuation))


def get_data(data, tag1, tag2) -> list:
    prep_data = data.findAll(tag1, tag2)
    return [item.text for item in prep_data]


def get_clear_tokens(text) -> str:
    tokens = nltk.tokenize.word_tokenize(text.lower())
    wnl = nltk.stem.WordNetLemmatizer()
    tokens_ = [wnl.lemmatize(token) for token in tokens if check_conditions(wnl.lemmatize(token))]
    return " ".join(tokens_)


def check_conditions(lemmatized_token: str) -> bool:
    bool_ = all([lemmatized_token not in words_to_avoid,
                nltk.pos_tag([lemmatized_token])[0][1] == "NN"])
    return bool_


with open("news.xml", "r") as f:
    file = f.read()

soup = BeautifulSoup(file, "xml")
headers = get_data(soup, "value", {"name": "head"})
texts = get_data(soup, "value", {"name": "text"})
dataset = [get_clear_tokens(text) for text in texts]

vectorizer = TfidfVectorizer(input='content', use_idf=True, lowercase=True, analyzer='word',
                             ngram_range=(1, 1), stop_words=None, vocabulary=None)
tfidf_matrix = vectorizer.fit_transform(dataset)
terms = vectorizer.get_feature_names_out()
matrix = pd.DataFrame(tfidf_matrix.toarray(), columns=terms, index=['txt1', 'txt2', 'txt3', 'txt4', 'txt5',
                                                                    'txt6', 'txt7', 'txt8', 'txt9', 'txt10'])

i = 1
for header in headers:
    print(header + ":")
    res_ = matrix.loc[f'txt{i}', :].reset_index().sort_values(by=[f"txt{i}", 'index'], ascending=False)
    res = res_["index"].iloc[:5].values
    print(" ".join(res))
    i += 1
