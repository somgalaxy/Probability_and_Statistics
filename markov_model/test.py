import random
import pickle



#Data Set
data_list = []
f_1 = open('C:/Users/jhchung/Desktop/Probability_and_Statistics/markov_model/data/convert.txt', 'r', encoding='UTF8')
f = open('C:/Users/jhchung/Desktop/Probability_and_Statistics/markov_model/test_data.txt', 'w', encoding='UTF8')
for i in range (1,46415):
    sant = f_1.readline()
    f.write(sant)
    data_list.append(sant)
data = (' '.join(data_list))
f.close()
f_1.close()
print('끝!')