from time import sleep
import pickle
import numpy
from json import load as jsonfload
import spacy
import os

nlp = spacy.load("en_core_web_trf") #Lemmatizer
current_dir = os.path.dirname(os.path.abspath(__file__))
current_dir = os.path.join(current_dir, "..")
current_dir = os.path.join(current_dir, "..")
data_dir = os.path.join(current_dir, "data")
raw_dir = os.path.join(data_dir, "raw")
intentsjson_dir = os.path.join(raw_dir, "school.json")
pretrained_dir = os.path.join(data_dir, "pretrained")
TrainedData_dir = os.path.join(pretrained_dir, "school.pickle")


# Normal data for transformation
try:
    with open(intentsjson_dir) as file:
        data = jsonfload(file)

except FileNotFoundError:
    print("intents.json the data file is missing!")
    exit()

def Transformthis():
    words = []
    labels = []
    docs_x = []
    docs_y = []
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            doc = nlp(pattern)
            wrds = [token.text.lower() for token in doc if not token.is_punct]
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])
            
        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        # Lemmatize the tokens using SpaCy
        wrds = [token.lemma_ for token in nlp(" ".join(doc)) if not token.is_punct]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)

    # Save the trained data!
    with open(TrainedData_dir, "wb") as f:
        pickle.dump((words, labels, training, output), f)
        print("DATA HAS BEEN TRANSFORMED!")

Transformthis()
