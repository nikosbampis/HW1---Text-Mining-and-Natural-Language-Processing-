
from nltk import FreqDist,word_tokenize
import math

from sklearn import datasets,model_selection

def BernoulliNBTrain(Docs,Classes):
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
        Vocabulary.update(set(tokens))
        bigDoc[classesDict[Docs[i][1]]]=bigDoc[classesDict[Docs[i][1]]]+list(set(tokens))
        logprior[classesDict[Docs[i][1]]]=logprior[classesDict[Docs[i][1]]]+1
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
    max=-100000
    clas=-1
    testDoc=set(testDoc)
    for i in range(len(Classes)):
        sum=0
        sum=math.log(model[1][i])
        for word in model[2]:
            aset={word}
            if(set(aset).issubset(testDoc)):
                sum=sum+math.log(model[0][word,Classes[i]])
            else:
                if(model[0][word,Classes[i]]<1):
                    sum=sum+math.log((1-model[0][word,Classes[i]]))
                else:
                    print(model[0][word,Classes[i]])
                    print(word)
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
model=BernoulliNBTrain(list(zip(x_train,y_train)),list(Classes))
    