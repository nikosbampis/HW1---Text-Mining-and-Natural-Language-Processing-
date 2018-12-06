<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
from nltk import FreqDist,word_tokenize
from sklearn import datasets,model_selection

def NaiveBayesTrain(Docs,Classes):
    
    Ndoc=len(Docs)
    # Initializing
    logprior=[]
    bigDoc=[]
    index=[]
    Vocabulary=set()
    for i in range(len(Classes)):
        index.append(i)
        bigDoc.append([])
        logprior.append(0)
    classesDict=dict(zip(Classes,index))
    for i in range(Ndoc):
        tokens=word_tokenize(Docs[i][0])
         # Create vocabulary
        Vocabulary.update(set(tokens))
        #Merge all sentences to one big document for each class
        bigDoc[classesDict[Docs[i][1]]]=bigDoc[classesDict[Docs[i][1]]] + tokens
        #calculate the possibility for every class
        logprior[classesDict[Docs[i][1]]]=logprior[classesDict[Docs[i][1]]] + 1
    for i in range(len(Classes)):
        logprior[i]=logprior[i]/Ndoc
        # Calculate the frequency of every word
        bigDoc[i]=FreqDist(w.lower() for w in bigDoc[i])  
    dictionaryLength=len(Vocabulary)
    likelihoodKey=[]
    likelihood=[]
    for word in Vocabulary:
        # Calculate the probability of a word being in a different class.
        for i in range(len(Classes)):
            count=bigDoc[i][word]
            likelihoodKey.append((word,Classes[i]))
            likelihood.append(math.log((count+1)/(len(bigDoc[i])+dictionaryLength)))
    # Change structure to a vocabulary with key and value pairs.
    likelihoodDict=dict(zip(likelihoodKey,likelihood))
    return  likelihoodDict,logprior,Vocabulary

def TestNaiveBayes(testdoc,model,Classes):
    max=-100000
    clas=-1
    testdoc=word_tokenize(testdoc)
     # Find class with the biggest probability.
    for i in range(len(Classes)):
        sum=0
        sum=model[1][i]
        print(sum)
        for word in testdoc:
            aset={word}
            if(set(aset).issubset(model[2])):
                sum=sum+model[0][word,Classes[i]]
        print(sum)
        if(sum>max):
            max=sum
            clas=Classes[i]
    return max,clas

textData = datasets.fetch_20newsgroups()
X = textData.data
y = textData.target
x_train, x_test, y_train, y_test = model_selection.train_test_split(X, y, random_state = 0)
Classes=set(y_train)
model=NaiveBayesTrain(list(zip(x_train,y_train)),list(Classes))
=======
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import nltk

def NaiveBayesTrain(Docs,Classes):
    
    Ndoc=len(Docs)

    # Initializing
    logprior=[]
    bigDoc=[]
    Vocabulary={}

    for i in range(len(Classes)):
        Nc=0
        bigDoc.append([])

        # Merge all sentences to one big documentation.
        for j in range(len(Docs)):

            # Create vocabulary searching for every documentation.

            Vocabulary=set(Vocabulary).union(set(Docs[j][0]))
            if(Docs[j][1]==Classes[i]):
                bigDoc[i]=bigDoc[i]+Docs[j][0]
                Nc=Nc+1

        # Calculate the probability of every class.
        logprior.append(math.log(Nc/Ndoc,10))

        # Calculate frequency of every word
        bigDoc[i]=nltk.FreqDist(w.lower() for w in bigDoc[i])
    dictionaryLength=len(Vocabulary)
    likelihoodKey=[]
    likelihood=[]
    for word in Vocabulary:

        # Calculate the probability of a word being in a different class.
        for i in range(len(Classes)):
            count=bigDoc[i][word]
            likelihoodKey.append((word,Classes[i]))
            likelihood.append(math.log((count+1)/(len(bigDoc[i])+dictionaryLength)))

    # Change structure to a vocabulary with key and value pairs.
    likelihoodDict=dict(zip(likelihoodKey,likelihood))
    return  likelihoodDict,logprior,Vocabulary

def NaiveBayesTest(testdoc,model,Classes):
    max=-100
    clas=-1

    # Find class with the bigger probability.
    for i in range(len(Classes)):
        sum=0
        sum=model[1][i]
        for word in testdoc:
            aset={word}
            if(set(aset).issubset(model[2])):
                sum=sum+model[0][word,Classes[i]]
        if(sum>max):
            max=sum
            clas=Classes[i]
    return max,clas

TheClasses=['-','+']
TrainSet=[(['just','plain','boring'],'-'),(['entirely','predictable','and','lacks','energy'],'-'),(['no','surprises','and','very','few','laughs'],'-'),(['very','powerful'],'+'),(['the','most','fun','movie','of','the','summer'],'+')]       
TrainSet[0][0]
model=NaiveBayesTrain(TrainSet,TheClasses)    
answer=NaiveBayesTest(['very','fun','and','powerful'],model,TheClasses)
print(answer)
>>>>>>> 781f37efdad497aeb9f014d2b180230913a72db9
