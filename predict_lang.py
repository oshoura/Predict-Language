import numpy as np
import textract


#get the Language trigram frequencies from the training data
langTrigramDic = {}
with open('languages.txt', 'r') as f:
    lang = ""
    for line in f:
        line = line[:-1]
        if line.isalpha():
            lang = line
        elif line == "":
            continue
        else:
            array = line.split()
            realArray = []
            for s in array:
                realArray.append(float(s))
            realArray = np.array(realArray)
            langTrigramDic[lang] = realArray

## main function  Path -> List(String)      
def returnLangSimiliratyResult(path):
    #open file
    unknown = textract.process(path).decode()
    #Perform cosine similiraty
    textTrigramFreq = openAndGetNormalizedTrigramFreqArray(unknown)
    cosineSimilarity = {}
    for lang, langTrigramFreq in langTrigramDic.items():
        num = textTrigramFreq.dot(langTrigramFreq)
        denom = np.linalg.norm(textTrigramFreq) * np.linalg.norm(langTrigramFreq)
        cosineSimilarity[lang] = num / denom
    
    result = []
    #return the top 3 languages with the highest cosine similarity
    sortedLangs = sorted(cosineSimilarity, key=cosineSimilarity.get, reverse=True)
    for lang in sortedLangs[:3]:
        result.append((lang, cosineSimilarity[lang]))
        
    return result

########### Helper functions ##########

#gets a Trigram look up dict where every trigram has unique code
trigramLookup = {}
posLeters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ')
for i in range(0, len(posLeters)):
    for j in range(0, len(posLeters)):
        for k in range(0, len(posLeters)):
            trigramLookup[posLeters[i] + posLeters[j] + posLeters[k]] = i * len(posLeters) * len(posLeters) + j * len(posLeters) + k


#opens a given file and returns a normalized trigram frequency array
# String -> Array
def openAndGetNormalizedTrigramFreqArray(text):
    #returns a list with all the trigrams in the text
    def allTrigramsInText(text):
        trigramList = []
        for i in range(0, len(text) - 2):
            trigramList.append(text[i:i+3].upper())
        return trigramList
    
    #removes excess whitespace, non alphabetical characters, and makes all letters uppercase
    def cleanText(text):
        text = ''.join(e for e in text if e.isalpha() or e == ' ')
        text = text.upper()
        text = text.replace('\n', ' ')
        text = text.replace('\r', ' ')
        text.strip()
        # remove double spaces
        while '  ' in text:
            text = text.replace('  ', ' ')
        return text

    #get the normalized trigram frequency array
    text = cleanText(text)
    trigram = allTrigramsInText(text)
    trigramFrequencies = [0] * len(posLeters) * len(posLeters) * len(posLeters)
    for trigram in trigram:
        trigramFrequencies[trigramLookup[trigram]] += 1
    #normalize trigram frequencies
    trigramFrequencies = np.array(trigramFrequencies)
    trigramFrequencies = trigramFrequencies / np.sum(trigramFrequencies)
    return trigramFrequencies
