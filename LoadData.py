import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import reuters, stopwords

def LoadData():
    stemmer = PorterStemmer()
    stop_words = set(stopwords.words('english'))

    doc = []
    for file_id in reuters.fileids():
        this_file = []

        for sen in reuters.sents(file_id):
            stem_word = [stemmer.stem(word) for word in sen if not word.lower() in stop_words]

            tokenize_word = [["<START>"]]
            tokenize_word.extend([nltk.word_tokenize(word) for word in stem_word if len(word)>2])
            tokenize_word.append(["<END>"])
            this_file.extend(tokenize_word)
        doc.extend(this_file)

    flat_doc = []
    for word in doc:
        flat_doc.extend(word)

    return flat_doc