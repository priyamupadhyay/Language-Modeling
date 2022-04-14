"""
Language Modeling Project
Name:
Roll No:
"""

import language_tests as test
from collections import Counter

project = "Language" # don't edit this

### WEEK 1 ###

'''
loadBook(filename)
#1 [Check6-1]
Parameters: str
Returns: 2D list of strs
'''
def loadBook(filename):
    with open(filename,'r') as f:
        listl=[]
        for line in f:
            strip_lines=line.strip()
            listli=strip_lines.split()
            #print(listli)
            if listli:
                m=listl.append(listli)
            else:
                continue
       #print(listl)
    return listl


'''
getCorpusLength(corpus)
#2 [Check6-1]
Parameters: 2D list of strs
Returns: int
'''
def getCorpusLength(corpus):
    count = 0
    for ele in corpus:
        count += len(ele)
    #print(count)
    return count


'''
buildVocabulary(corpus)
#3 [Check6-1]
Parameters: 2D list of strs
Returns: list of strs
'''
def buildVocabulary(corpus):
    list = []
    for i in range(len(corpus)):
        for j in range(len(corpus[i])):
            if corpus[i][j] not in list:
                list.append(corpus[i][j])
            #print(corpus[i][j])
    return list


'''
countUnigrams(corpus)
#4 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to ints
'''
def countUnigrams(corpus):
    dict = {}
    for i in range(len(corpus)):
        for j in range(len(corpus[i])):
            temp = corpus[i][j]
            if temp in dict:
                dict[temp] += 1
            else:
                dict[temp] = 1
                #dict[temp] = count
    #print(dict)
    return dict


'''
getStartWords(corpus)
#5 [Check6-1]
Parameters: 2D list of strs
Returns: list of strs
'''
def getStartWords(corpus):
    lst = []
    for i in range(len(corpus)):
        for j in range(len(corpus[i])):
            temp = corpus[i][0]
            if temp not in lst:
                lst.append(temp)
    #print(lst)
    return lst


'''
countStartWords(corpus)
#5 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to ints
'''
def countStartWords(corpus):
    dict = {}
    for i in range(len(corpus)):
        temp = corpus[i][0]
        if temp in dict:
            dict[temp] += 1
        else:
            dict[temp] = 1
    #print(dict)
    return dict


'''
countBigrams(corpus)
#6 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to (dicts mapping strs to ints)
'''
def countBigrams(corpus):
    dict = {}
    for i in range(len(corpus)):
        for j in range(len(corpus[i])-1):
            if corpus[i][j] not in dict:
                dict[corpus[i][j]] = {}
                dict[corpus[i][j]][corpus[i][j+1]] = 1
            else:
                if corpus[i][j+1] not in dict[corpus[i][j]]:
                    dict[corpus[i][j]][corpus[i][j+1]] = 1
                else:
                    dict[corpus[i][j]][corpus[i][j+1]] += 1
    #print(dict)
    return dict


### WEEK 2 ###

'''
buildUniformProbs(unigrams)
#1 [Check6-2]
Parameters: list of strs
Returns: list of floats
'''
def buildUniformProbs(unigrams):
    le = len(unigrams)
    lst = []
    for i in range(le):
        lst.append(1/le)
    return lst


'''
buildUnigramProbs(unigrams, unigramCounts, totalCount)
#2 [Check6-2]
Parameters: list of strs ; dict mapping strs to ints ; int
Returns: list of floats
'''
def buildUnigramProbs(unigrams, unigramCounts, totalCount):
    list=[]
    for i in unigrams:
        if i in unigramCounts:
            list.append(unigramCounts[i]/totalCount)
        else:
            list.append(0)
    return list


'''
buildBigramProbs(unigramCounts, bigramCounts)
#3 [Check6-2]
Parameters: dict mapping strs to ints ; dict mapping strs to (dicts mapping strs to ints)
Returns: dict mapping strs to (dicts mapping strs to (lists of values))
'''
def buildBigramProbs(unigramCounts, bigramCounts):
    d = {}
    for word in bigramCounts:
        lst = []
        lst1 = []
        for i,j in bigramCounts[word].items():
            lst.append(i)
            '''if j/unigramCounts[word] == 1.0:
                lst1.append(j//unigramCounts[word])
            if j/unigramCounts[word] < 1.0:
                lst1.append(j/unigramCounts[word])'''
            lst1.append(j/unigramCounts[word])
            d1 = {}
            d1["words"] = lst
            d1["probs"] = lst1
        d[word] = d1
    #print(d)
    return d


'''
getTopWords(count, words, probs, ignoreList)
#4 [Check6-2]
Parameters: int ; list of strs ; list of floats ; list of strs
Returns: dict mapping strs to floats
'''
def getTopWords(count, words, probs, ignoreList):
    dict = {}
    for ele in range(len(words)):
        if words[ele] not in ignoreList:
            dict[words[ele]] = probs[ele]
    top = Counter(dict)
    top = top.most_common(count)
    dict = {}
    for i, j in top:
        dict[i] = j
    #print(dict)
    return dict


'''
generateTextFromUnigrams(count, words, probs)
#5 [Check6-2]
Parameters: int ; list of strs ; list of floats
Returns: str
'''
import random
from random import choices
def generateTextFromUnigrams(count, words, probs):
    lst = choices(words,k = count, weights=probs)
    sentence = " ".join(lst)
    return sentence


'''
generateTextFromBigrams(count, startWords, startWordProbs, bigramProbs)
#6 [Check6-2]
Parameters: int ; list of strs ; list of floats ; dict mapping strs to (dicts mapping strs to (lists of values))
Returns: str
'''
def generateTextFromBigrams(count, startWords, startWordProbs, bigramProbs):
    sentence = ""
    wrd = choices(startWords, weights = startWordProbs)
    #choice = random.choices(startWords, weights = startWordProbs)
    sentence += wrd[0]
    lst = sentence
    for i in range(count-1):
        if lst != '.':
            if lst in bigramProbs:
                lst = choices(bigramProbs[lst]["words"], weights = bigramProbs[lst]["probs"])[0]
                sentence = sentence + ' ' + lst
        #print(sentence)
        else:
            wrd = choices(startWords, weights = startWordProbs)
            sentence =sentence+' '+ wrd[0]
            lst = wrd[0]
    #print(sentence)
    return sentence


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
    cnt = getCorpusLength(corpus)
    uniqwrd = buildVocabulary(corpus)
    unigrms = countUnigrams(corpus)
    probilities = buildUnigramProbs(uniqwrd, unigrms, cnt)
    output = getTopWords(50, uniqwrd, probilities, ignore)
    barPlot(output, "Top 50 words")
    return


'''
graphTopStartWords(corpus)
#4 [Hw6]
Parameters: 2D list of strs
Returns: None
'''
def graphTopStartWords(corpus):
    star_wrd = getStartWords(corpus)
    cnt = countStartWords(corpus)
    probilities = buildUnigramProbs(star_wrd, cnt, len(corpus))
    output = getTopWords(50, star_wrd, probilities, ignore)
    barPlot(output, "Top 50 start words")
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

    plt.bar(names, values, color = 'green')

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
    '''print("\n" + "#"*15 + " WEEK 1 TESTS " +  "#" * 16 + "\n")
    test.week1Tests()
    print("\n" + "#"*15 + " WEEK 1 OUTPUT " + "#" * 15 + "\n")
    test.runWeek1()'''
    '''test.testLoadBook()
    test.testGetCorpusLength()
    test.testBuildVocabulary()
    test.testCountUnigrams()
    test.testGetStartWords()
    test.testCountStartWords()
    test.testCountBigrams()
    test.testBuildUniformProbs()
    test.testBuildUnigramProbs()
    test.testBuildBigramProbs()
    test.testGetTopWords()
    test.testGenerateTextFromUnigrams()
    test.testGenerateTextFromBigrams()'''
    ## Uncomment these for Week 2 ##
    
    '''print("\n" + "#"*15 + " WEEK 2 TESTS " +  "#" * 16 + "\n")
    test.week2Tests()
    print("\n" + "#"*15 + " WEEK 2 OUTPUT " + "#" * 15 + "\n")
    test.runWeek2()'''
    

    ## Uncomment these for Week 3 ##
    print("\n" + "#"*15 + " WEEK 3 OUTPUT " + "#" * 15 + "\n")
    test.runWeek3()