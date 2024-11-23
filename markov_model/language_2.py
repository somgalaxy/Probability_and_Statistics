import random
import pickle



#Data Set
data_list = []
f = open('C:/Users/jhchung/Desktop/Probability_and_Statistics/markov_model/data/convert.txt', 'r', encoding='UTF8')
#f_1= open('C:/Users/jhchung/Desktop/Probability_and_Statistics/markov_model/test_data.txt', 'w', encoding='UTF8')
for i in range (1,46415):
    sant = f.readline()
#    f_1.write(sant)
    data_list.append(sant)
data = (' '.join(data_list))
f.close()
#f_1.close()

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
    return model

model_1 = markov_modle(data, 4)

with open('C:/Users/jhchung/Desktop/Probability_and_Statistics/markov_model/data/model_1.pickle', 'wb') as f:
    pickle.dump(model_1, f)






def predict(model, current):
    if current not in model:
        # 이전 문자열이 모델에 없을 경우, 임의의 문자열 반환
        return random.choice(list(model.keys()))[0]
    # 이전 문자열이 모델에 있을 경우, 다음 문자열 예측
    next_chars = model[current]
    total = sum(next_chars.values())
    probabilities = {k: v/total for k, v in next_chars.items()}
    return random.choices(list(probabilities.keys()), list(probabilities.values()))[0]

with open('C:/Users/jhchung/Desktop/Probability_and_Statistics/markov_model/data/model_1.pickle', 'rb') as f:
    model_1 = pickle.load(f)

# 테스트
current = input('문자 입력: ')
a = int(input("문장의 길이(글자 수)"))
a_sant = current
a_paredict = predict(model_1, a_sant[-1:])
print('입력된 문자:', current)
print('1개로 예측된 후행 문자:', predict(model_1, current[-1:]))

for i in range (0,a):
    a_paredict = predict(model_1, a_sant[-1:])
    a_sant = a_sant + a_paredict
print(a_sant)



