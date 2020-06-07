import predictor as pred
import json

lista = []
dictio = {}

with open("cleaned_file.txt") as f:
    for line in f:
        word_list = line.split()
        for word in word_list:
            if(len(word)==1):
                continue
            pred.prepare_input(word.lower())
            prediction = pred.predict_completions(word, 1)[0]
            if(len(prediction)==1):
                prediction = ""
            dictio[word] = prediction

with open('hint_products.json', 'w') as filename:
    json.dump(dictio, filename)