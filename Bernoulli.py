
from nltk import FreqDist,word_tokenize
import math

from sklearn import datasets,model_selection

def BernoulliNBTrain(Docs,Classes):
    # Initializing
    Ndoc=len(Docs)
    index=[]
    logprior=[]
    bigDoc=[]
    likelihoodKey=[]
    likelihood=[]
    Vocabulary=set()
    for i in range(len(Classes)):
        index.append(i)
        bigDoc.append([])
        logprior.append(0)
    classesDict=dict(zip(Classes,index))
    for i in range(len(Docs)):
        tokens = word_tokenize(Docs[i][0])
        tokens = [w.lower() for w in tokens]
        #update the vocabulary
        Vocabulary.update(set(tokens))
        #we transforming the tokens from list to set and back to list so the duplicates will be eliminated
        bigDoc[classesDict[Docs[i][1]]]=bigDoc[classesDict[Docs[i][1]]]+list(set(tokens))
        logprior[classesDict[Docs[i][1]]]=logprior[classesDict[Docs[i][1]]]+1
    #Calculate the possibility foreach word in the vocabulary for every class
    for i in range(len(Classes)):
        bigDoc[i]=FreqDist(w.lower() for w in bigDoc[i])
        for word in Vocabulary:
            count=bigDoc[i][word]
            likelihoodKey.append((word,Classes[i]))
            likelihood.append((count+1)/(logprior[i]+2))
        logprior[i]=logprior[i]/Ndoc
    likelihoodDict=dict(zip(likelihoodKey,likelihood))
    return  likelihoodDict,logprior,Vocabulary,bigDoc


def BernoulliNBTest(testDoc,model,Classes):
    max=None
    clas=-1
    testDoc=set(testDoc)
    #we want the class with the maximum sum
    for i in range(len(Classes)):
        sum=0
        sum=math.log(model[1][i])
        for word in model[2]:
            aset={word}
            if(set(aset).issubset(testDoc)):
                sum=sum+math.log(model[0][word,Classes[i]])
            else:
                sum=sum+math.log((1-model[0][word,Classes[i]]))
        if(max==None):
            max=sum
            clas=Classes[i]
        elif(sum>max):
            max=sum
            clas=Classes[i]
    return max,clas


textData = datasets.fetch_20newsgroups()
X = textData.data
y = textData.target
x_train, x_test, y_train, y_test = model_selection.train_test_split(X, y, random_state = 0)
Classes=set(y_train)
model=BernoulliNBTrain(list(zip(x_train,y_train)),list(Classes))
    