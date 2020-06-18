import numpy as np
from nltk.tokenize import RegexpTokenizer
from keras.models import Sequential, load_model
from keras.layers import LSTM
from keras.layers.core import Dense, Activation
from keras.optimizers import RMSprop
import matplotlib.pyplot as plt
import pickle
import heapq

path = 'cleaned_file.txt'
text = open(path).read().lower()

# podzielenie tekstu na pojedyncze slowa bez specjalnych znakow
tokenizer = RegexpTokenizer(r'\w+')     
words = tokenizer.tokenize(text)

# unikalne slowa w formie key: value, key to slowo, value to "pozycja tego slowa"
unique_words = np.unique(words)         
unique_word_index = dict((c, i) for i, c in enumerate(unique_words))

# bazowanie na pierwszym slowie
WORD_LENGTH = 1                         
prev_words = []
next_words = []
for i in range(len(words) - WORD_LENGTH):
    prev_words.append(words[i:i + WORD_LENGTH])
    next_words.append(words[i + WORD_LENGTH])

X = np.zeros((len(prev_words), WORD_LENGTH, len(unique_words)), dtype=bool) # one hot-encoding
Y = np.zeros((len(next_words), len(unique_words)), dtype=bool)
for i, each_words in enumerate(prev_words):
    for j, each_word in enumerate(each_words):
        X[i, j, unique_word_index[each_word]] = 1
    Y[i, unique_word_index[next_words[i]]] = 1

# budowanie modelu LSTM z 128 neuronami, uzycie fk softmax 
model = Sequential()
model.add(LSTM(128, input_shape=(WORD_LENGTH, len(unique_words))))
model.add(Dense(len(unique_words)))
model.add(Activation('softmax'))

# trenowanie modelu
optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
history = model.fit(X, Y, validation_split=0.05, batch_size=128, epochs=2, shuffle=True).history

# przekazanie inputu do pozniejszych sugestii
def prepare_input(text):
    x = np.zeros((1, WORD_LENGTH, len(unique_words)))
    for t, word in enumerate(text.split()):
        try:
            x[0, t, unique_word_index[word]] = 1
        except KeyError:
            pass
    return x

# wybranie najlepszych slow na podstawie probki
def sample(preds, top_n=3):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds)
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)

    return heapq.nlargest(top_n, range(len(preds)), preds.take)

# rzeczywiste predykcje
def predict_completions(text, n=3):
    if text == "":
        return("0")
    x = prepare_input(text)
    preds = model.predict(x, verbose=0)[0]
    next_indices = sample(preds, n)
    return [unique_words[idx] for idx in next_indices]
