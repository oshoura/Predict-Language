# Predict-Language
Simple CLI program that is given an input document with a list of files. 

Directions: Provide a .txt to the program with the a list of language names and the associated file that contains that language.
i.e. 
English englishdoc.txt
French frenchdoc.txt
German germandoc.txt

Then, within that same list (no order is necassary), provide some documents that you want to detect what language they are in, by tagging them as unkown.
i.e.
Unknown languagedoc.txt
Unknown languageText.txt

Finally, the program also takes in a second file, where it will append it's results to, listing the unknown
document names and what possible languages it could be in associated with the programs's confidence for each prediction
