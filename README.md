# General Information

Key term extraction, also known as keyword extraction, is an important Natural Language Processing (NLP) task 
that makes it possible to automatically identify terms that best describe the subject of a document.

Key term extraction is the core of the content-based advertising systems used by search engines. 
This approach is used to find the relevant keywords on a webpage and then show the ads based on those keywords. 
The extraction quality is a cornerstone for these tasks. A 10% improvement in quality leads to an almost 10% increase 
in click-through rate, directly increasing the advertisement performance.

What words can describe the subject of a piece of text accurately? 
It's safe to assume that they are the most frequent words, but it can be a little more complicated than that!

Extracting keywords can help you get to the text meaning. Also, It can help you with splitting texts into different categories.

In this project, you will learn how to extract relevant words from a collection of news stories. 
There are many different ways to do it, but we will focus on frequencies, part-of-speech search, and TF-IDF methods. 
Note that each method can yield the results with varying degrees of accuracy for different texts. 
In reality, it is always good to try various methods and choose the best.

## Description

Key terms extractor utilizes TF-IDF approach.\
It is used to calculate how important a word is for a document in a text collection. 
Search engines use this measure to score and rank the documents according to a user's query. 
It is also frequently used for text classification and text summarization, fundamental NLP tasks. 
The method is not computationally expensive and yields excellent results for such tasks.

The technique is based on two assumptions:
* Frequent words have more weight in the document.
* The smaller the number of documents that contain the word, the more important the word is for the document that contains it.

## Howto

Launch program by input in CLI:\
python key_terms.py\
so, this program:

1. Read an XML-file containing stories and headlines.
2. Extract the headers and the text.
3. Tokenize each text.
4. Lemmatize each word in each story.
5. Get rid of punctuation, stopwords, and non-nouns with the help of NLTK.
6. Count the TF-IDF metric for each word in all stories, i.e. apply it to the whole collection of news documents.
7. Pick the five best scoring words.
8. Print each story's headline and the five most frequent words in descending order. Take a look at the sample output below. Display the titles and keywords in the same order they are presented in the file.