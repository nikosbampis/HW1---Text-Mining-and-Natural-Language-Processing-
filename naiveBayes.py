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