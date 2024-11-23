import random
import pickle



#Data Set
with open('C:/Users/jhchung/Desktop/Probability_and_Statistics/markov_model/data/KakaoData.txt', 'r', encoding='UTF8') as f:
    data = f.readline()


def markov_modle(data, order):
    model = {}
    for i in range(len(data)-order):
    #Save to dictionarry
        current = data[i:i+order]
        next_char = data[i+order] 
        if current not in model:
            model[current] = {}
        if next_char not in model[current]:
            model[current][next_char] = 0
        model[current][next_char] += 1
        print(model)
    return model

model_1 = markov_modle(data, 1)

with open('C:/Users/jhchung/Desktop/Probability_and_Statistics/markov_model/data/model_1.pickle', 'wb') as f:
    pickle.dump(model_1, f)


print(model_1)


