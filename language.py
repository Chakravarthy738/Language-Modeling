"""
Language Modeling Project
Name:
Roll No:
"""

from this import d
from matplotlib import lines
from pyparsing import line
import language_tests as test

project = "Language" # don't edit this

### WEEK 1 ###

'''
loadBook(filename)
#1 [Check6-1]
Parameters: str
Returns: 2D list of strs
'''
def loadBook(filename):
    book=open(filename,"r")
    lines= book.read()
    corpus=[]
    for i in lines.split("\n"):
        if len(i) > 0:
           line=i.split(" ")
           corpus.append(line)   
    return corpus


'''
getCorpusLength(corpus)
#2 [Check6-1]
Parameters: 2D list of strs
Returns: int
'''
def getCorpusLength(corpus):
    total_length =sum(len(Row) for Row in corpus)
    return total_length


'''
buildVocabulary(corpus)
#3 [Check6-1]
Parameters: 2D list of strs
Returns: list of strs
'''
def buildVocabulary(corpus):
    a= list(set(i for j in corpus for i in j))
    return a


'''
countUnigrams(corpus)
#4 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to ints
'''
def countUnigrams(corpus):
    c={}
    d=list(i for j in corpus for i in j)
    for i in d:
        if i not in c:
            c[i]= d.count(i)     
    return c


'''
getStartWords(corpus)
#5 [Check6-1]
Parameters: 2D list of strs
Returns: list of strs
'''
def getStartWords(corpus):
    a=[]
    for i in corpus:
        if i[0] not in a:
            a.append(i[0])
    return a
    

'''
countStartWords(corpus)
#5 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to ints
'''
def countStartWords(corpus):
    dicts={}
    for i in corpus:
        if i[0] not in dicts:
            dicts[i[0]]=1
        else:
            dicts[i[0]]+=1
    return dicts


'''
countBigrams(corpus)
#6 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to (dicts mapping strs to ints)
'''
def countBigrams(corpus):
    dicts={}
    for i in corpus:
        for j in range(len(i)-1):
            sentence1=i[j]
            sentence2=i[j+1]
            if sentence1 not in dicts:
                dicts[sentence1]={}
            if sentence2 not in dicts[sentence1]:
                dicts[sentence1][sentence2]=1
            else:
                dicts[sentence1][sentence2]+=1
    return dicts

        
### WEEK 2 ###

'''
buildUniformProbs(unigrams)
#1 [Check6-2]
Parameters: list of strs
Returns: list of floats
'''
def buildUniformProbs(unigrams):
    probs=[1/len(unigrams)]*len(unigrams)
    return probs


'''
buildUnigramProbs(unigrams, unigramCounts, totalCount)
#2 [Check6-2]
Parameters: list of strs ; dict mapping strs to ints ; int
Returns: list of floats
'''
def buildUnigramProbs(unigrams, unigramCounts, totalCount):
    probs=[]
    i=0
    for j in range(len(unigrams)):
        if unigrams[j] in unigramCounts:
            i=unigramCounts[unigrams[j]]
            probability=i/totalCount
            probs.append(probability) 
        else:
            probs.append(0)
    return probs


'''
buildBigramProbs(unigramCounts, bigramCounts)
#3 [Check6-2]
Parameters: dict mapping strs to ints ; dict mapping strs to (dicts mapping strs to ints)
Returns: dict mapping strs to (dicts mapping strs to (lists of values))
'''
def buildBigramProbs(unigramCounts, bigramCounts):
    newdict={}
    for prevword in bigramCounts.keys():
        sentence=[]
        Probs=[]
        temp={}
        for key,value in bigramCounts[prevword].items():
            sentence.append(key)
            prob=value/unigramCounts[prevword]
            Probs.append(prob)
            temp["words"]=sentence
            temp["probs"]=Probs
        newdict[prevword]=temp
    return newdict

    return


'''
getTopWords(count, words, probs, ignoreList)
#4 [Check6-2]
Parameters: int ; list of strs ; list of floats ; list of strs
Returns: dict mapping strs to floats
'''
def getTopWords(count, words, probs, ignoreList):
    import operator
    dicts1={}
    for j in range(len(words)):
        if words[j] not in ignoreList:
            dicts1[words[j]]=probs[j]
    Topwords = dict(sorted(dicts1.items(), key=operator.itemgetter(1), reverse=True)[:count])
    return Topwords


'''
generateTextFromUnigrams(count, words, probs)
#5 [Check6-2]
Parameters: int ; list of strs ; list of floats
Returns: str
'''
from random import choices
def generateTextFromUnigrams(count, words, probs):
    Text=""
    for i in range(count):
        sentence=choices(words, weights=probs)
        Text=Text+" "+sentence[0]
    return Text


'''
generateTextFromBigrams(count, startWords, startWordProbs, bigramProbs)
#6 [Check6-2]
Parameters: int ; list of strs ; list of floats ; dict mapping strs to (dicts mapping strs to (lists of values))
Returns: str
'''
def generateTextFromBigrams(count, startWords, startWordProbs, bigramProbs):
    Text=""
    prevword=""
    for i in range(count):
        if Text=="" or prevword==".":
            sentence=choices(startWords, weights=startWordProbs)
            Text=Text+" "+sentence[0]
            prevword=sentence[0]
        else:
            sentence=choices(bigramProbs[prevword]["words"], weights=bigramProbs[prevword]["probs"])
            Text=Text+" "+sentence[0]
            prevword=sentence[0]
    return Text


### WEEK 3 ###

ignore = [ ",", ".", "?", "'", '"', "-", "!", ":", ";", "by", "around", "over",
           "a", "on", "be", "in", "the", "is", "on", "and", "to", "of", "it",
           "as", "an", "but", "at", "if", "so", "was", "were", "for", "this",
           "that", "onto", "from", "not", "into" ]

'''
graphTop50Words(corpus)
#3 [Hw6]
Parameters: 2D list of strs
Returns: None
'''
def graphTop50Words(corpus):
    return


'''
graphTopStartWords(corpus)
#4 [Hw6]
Parameters: 2D list of strs
Returns: None
'''
def graphTopStartWords(corpus):
    return


'''
graphTopNextWords(corpus, word)
#5 [Hw6]
Parameters: 2D list of strs ; str
Returns: None
'''
def graphTopNextWords(corpus, word):
    return


'''
setupChartData(corpus1, corpus2, topWordCount)
#6 [Hw6]
Parameters: 2D list of strs ; 2D list of strs ; int
Returns: dict mapping strs to (lists of values)
'''
def setupChartData(corpus1, corpus2, topWordCount):
    return


'''
graphTopWordsSideBySide(corpus1, name1, corpus2, name2, numWords, title)
#6 [Hw6]
Parameters: 2D list of strs ; str ; 2D list of strs ; str ; int ; str
Returns: None
'''
def graphTopWordsSideBySide(corpus1, name1, corpus2, name2, numWords, title):
    return


'''
graphTopWordsInScatterplot(corpus1, corpus2, numWords, title)
#6 [Hw6]
Parameters: 2D list of strs ; 2D list of strs ; int ; str
Returns: None
'''
def graphTopWordsInScatterplot(corpus1, corpus2, numWords, title):
    return


### WEEK 3 PROVIDED CODE ###

"""
Expects a dictionary of words as keys with probabilities as values, and a title
Plots the words on the x axis, probabilities as the y axis and puts a title on top.
"""
def barPlot(dict, title):
    import matplotlib.pyplot as plt

    names = []
    values = []
    for k in dict:
        names.append(k)
        values.append(dict[k])

    plt.bar(names, values)

    plt.xticks(rotation='vertical')
    plt.title(title)

    plt.show()

"""
Expects 3 lists - one of x values, and two of values such that the index of a name
corresponds to a value at the same index in both lists. Category1 and Category2
are the labels for the different colors in the graph. For example, you may use
it to graph two categories of probabilities side by side to look at the differences.
"""
def sideBySideBarPlots(xValues, values1, values2, category1, category2, title):
    import matplotlib.pyplot as plt

    w = 0.35  # the width of the bars

    plt.bar(xValues, values1, width=-w, align='edge', label=category1)
    plt.bar(xValues, values2, width= w, align='edge', label=category2)

    plt.xticks(rotation="vertical")
    plt.legend()
    plt.title(title)

    plt.show()

"""
Expects two lists of probabilities and a list of labels (words) all the same length
and plots the probabilities of x and y, labels each point, and puts a title on top.
Note that this limits the graph to go from 0x0 to 0.02 x 0.02.
"""
def scatterPlot(xs, ys, labels, title):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()

    plt.scatter(xs, ys)

    # make labels for the points
    for i in range(len(labels)):
        plt.annotate(labels[i], # this is the text
                    (xs[i], ys[i]), # this is the point to label
                    textcoords="offset points", # how to position the text
                    xytext=(0, 10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center

    plt.title(title)
    plt.xlim(0, 0.02)
    plt.ylim(0, 0.02)

    # a bit of advanced code to draw a y=x line
    ax.plot([0, 1], [0, 1], color='black', transform=ax.transAxes)

    plt.show()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    #print("\n" + "#"*15 + " WEEK 1 TESTS " +  "#" * 16 + "\n")
    #test.week1Tests()
    #print("\n" + "#"*15 + " WEEK 1 OUTPUT " + "#" * 15 + "\n")
    #test.runWeek1()
    #test.testLoadBook()
    #test.testGetCorpusLength()
    #test.testBuildVocabulary()
    #test.testCountUnigrams()
    #test.testGetStartWords()
    #test.testCountStartWords()
    #test.testCountBigrams()
    

    ## Uncomment these for Week 2 ##

    print("\n" + "#"*15 + " WEEK 2 TESTS " +  "#" * 16 + "\n")
    test.week2Tests()
    print("\n" + "#"*15 + " WEEK 2 OUTPUT " + "#" * 15 + "\n")
    test.runWeek2()
    #test.testBuildUniformProbs()
    #test.testBuildUnigramProbs()
    #test.testBuildBigramProbs()
    #test.testGetTopWords()
    #test.testGenerateTextFromUnigrams()
    test.testGenerateTextFromBigrams()



    ## Uncomment these for Week 3 ##
"""
    print("\n" + "#"*15 + " WEEK 3 OUTPUT " + "#" * 15 + "\n")
    test.runWeek3()
"""