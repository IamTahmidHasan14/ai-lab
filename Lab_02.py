#python dictionary
dataset={
    'k':[[208,136],[196,119],[184,114]], #wrestler
    'r':[[170,67],[185,81]] #footballer
}
#print(dataset)

import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

def scatter_plot(new_feat):

    for i in dataset:
        for j in dataset[i]:
            plt.scatter(j[0],j[1],color=i)
    plt.scatter(new_feat[0],new_feat[1],s=100,color='b')
    plt.show()

import numpy as np
from collections import Counter

def knn(data,predict,k):
    distance=[]
    for group in data:
        for features in data[group]:
            ecd=np.linalg.norm(np.array(features)-np.array(predict))
            distance.append([ecd,group])
    print(distance)
    votes=[i[1] for i in sorted(distance)[:k]]
    print(votes)
    vote_result=Counter(votes).most_common(1)[0][0]
    return vote_result

while True:
    new_one=input('Enter new sample [height,weight]:').split(',')
    new_sample=[]
    new_sample.append(int(new_one[0]))
    new_sample.append(int(new_one[1]))
    if new_sample==[0,0]:
        break
    else:
        print(new_sample)
        scatter_plot(new_sample)
        result=knn(dataset,new_sample,3)
        if result=='k':
            print('New member => Wrestler')
        else:
            print('New member => Footballer')
            
#next lab report
    #Illustrate knowledge discovery mechanism by appling KNN
            
#5 december -> lab quiz test in python