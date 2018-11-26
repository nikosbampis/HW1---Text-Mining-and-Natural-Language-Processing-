# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import nltk

def NaiveBayesTrain(Docs,Classes):
    
    Ndoc=len(Docs)
    #αρχικοποιήσεις
    logprior=[]
    bigDoc=[]
    Vocabulary={}
    for i in range(len(Classes)):
        Nc=0
        bigDoc.append([])
        #ενώνω όλες τις προτάσεις της κλάσης σε ένα μεγάλο doc
        for j in range(len(Docs)):
            #δημιουργούμε το λεξικό ψάχνοντας,ενω όλα τα doc
            Vocabulary=set(Vocabulary).union(set(Docs[j][0]))
            if(Docs[j][1]==Classes[i]):
                bigDoc[i]=bigDoc[i]+Docs[j][0]
                Nc=Nc+1
        #υπολογίζουμε την πιθανότητα της κάθε κλάσης
        logprior.append(math.log(Nc/Ndoc,10))
        #παίρνουμε την συχνότητα εμφάνισης κάθε λέξης
        bigDoc[i]=nltk.FreqDist(w.lower() for w in bigDoc[i])
    dictionaryLength=len(Vocabulary)
    likelihoodKey=[]
    likelihood=[]
    for word in Vocabulary:
        #υπολογίζουμε για κάθε λέξη την πιθανότητα να βρήσκεται σε κάθε κλάση
        for i in range(len(Classes)):
            count=bigDoc[i][word]
            likelihoodKey.append((word,Classes[i]))
            likelihood.append(math.log((count+1)/(len(bigDoc[i])+dictionaryLength)))
    #αλλάζουμε την δομή σε λεξικό με κλειδί (λέξη,κλάση) και value την πιθανότητα
    likelihoodDict=dict(zip(likelihoodKey,likelihood))
    return  likelihoodDict,logprior,Vocabulary

def TestNaiveBayes(testdoc,model,Classes):
    max=-100
    clas=-1
    #βρίσκομε ποιά κλάση έχει την μεγαλύτερη πιθανότητα
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
answer=TestNaiveBayes(['very','fun','and','powerful'],model,TheClasses)    
print(answer)