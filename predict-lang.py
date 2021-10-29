import os
import numpy as np
import argparse


########### Helper functions ##########



#gets a Trigram look up dict where every trigram has unique code
trigramLookup = {}
posLeters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ')
for i in range(0, len(posLeters)):
    for j in range(0, len(posLeters)):
        for k in range(0, len(posLeters)):
            trigramLookup[posLeters[i] + posLeters[j] + posLeters[k]] = i * len(posLeters) * len(posLeters) + j * len(posLeters) + k


#opens a given file and returns a normalized trigram frequency array
def openAndGetNormalizedTrigramFreqArray(inputText):
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

    #open the file
    with open(inputText, 'r') as f:
        text = f.read()
        text = cleanText(text)
        trigram = allTrigramsInText(text)
        trigramFrequencies = [0] * len(posLeters) * len(posLeters) * len(posLeters)
        for trigram in trigram:
            trigramFrequencies[trigramLookup[trigram]] += 1
        #normalize trigram frequencies
        trigramFrequencies = np.array(trigramFrequencies)
        trigramFrequencies = trigramFrequencies / np.sum(trigramFrequencies)
    return trigramFrequencies


#appends to the bottom of an output text file, the top 3 languages with the highest cosine similarity
def createOutputFile(cosineSimilarity, inputText, outputFile):
    with open(outputFile, "a") as f:
        f.write("\n" + inputText + " - The most probable languages of the document and how confident the program is:\n")
        sortedLangs = sorted(cosineSimilarity, key=cosineSimilarity.get, reverse=True)
        for lang in sortedLangs[:3]:
            f.write(lang + " " + str(cosineSimilarity[lang]) + "\n")
    return

#################### MAIN ####################

def main(inputFile, outputFile):
    #open inputFile and get the unkown and known files and their trigram frequencies
    unknownFiles = []
    langTrigramDic = {}
    with open(inputFile, 'r') as f:
        for line in f:
            try:
                tag = line.split()[0]
                file = line.split()[1]
            except:
                continue
            if tag == 'Unknown':
                unknownFiles.append(file)
            elif tag in langTrigramDic.keys():
                langTrigramDic[tag] += openAndGetNormalizedTrigramFreqArray(file)
            else:
                langTrigramDic[tag] = openAndGetNormalizedTrigramFreqArray(file)


    #perform cosine similarity on all the unknown files 
    for unkownFile in unknownFiles:
        textTrigramFreq = openAndGetNormalizedTrigramFreqArray(unkownFile)
        cosineSimilarity = {}
        for lang, langTrigramFreq in langTrigramDic.items():
            num = textTrigramFreq.dot(langTrigramFreq)
            denom = np.linalg.norm(textTrigramFreq) * np.linalg.norm(langTrigramFreq)
            cosineSimilarity[lang] = num / denom
        createOutputFile(cosineSimilarity, unkownFile, outputFile)
        
    print("Appended the input files and their predicted languages from " + inputFile + " to " + outputFile)
    return


if __name__ == "__main__":
    #initialize the parser
    parser = argparse.ArgumentParser(description='Predict language')

    #add args
    parser.add_argument('input',  help='contains the names of all the files for input')
    parser.add_argument('output',  help='contains the output of the program')
    #parse args
    args = parser.parse_args()

    main(args.input, args.output)
    #main('input.txt', 'output.txt')

