import tkinter as tk
from tkinter import filedialog
import os
from predictLang import returnLangSimiliratyResult

page = tk.Tk(screenName="Language predictor", baseName="Language predictor", className="Language predictor", useTk=1)

#A function that formats the results of the prediction
# Path -> String
def formatResults(filename):
    results = returnLangSimiliratyResult(filename)
    s = "Here are the algorithim's top predicted languages for the file :\n"
    for tuple in results:
        s += tuple[0] + " : " + str(round(tuple[1],2)) + "\n"
    return s

filename = None

#The title and header of the window
title = tk.Label(page, text="Language Predictor.",  font=("Helvetica", 16))
title.place(relx=.5, y = 20,anchor= "center")
header = tk.Label(page, text="Welcome, please select a file.", font=("Helvetica", 16))
header.place(relx=.5, y = 50,anchor= "center")


page.result = "Here is where the results will be displayed"


#creating a button to load the file and then display the predicted languages and their confidence in a label
def loadFile():
    filename = filedialog.askopenfilename(title="Select file", filetypes=(("Text files", "*.txt *.doc *.docx *.pdf"), ("All files", "*.*")))
    resultsLbl.config(text = formatResults(filename))
    file = tk.Label(page, text=os.path.basename(filename), font=("Helvetica", 10))
    file.place(relx=.5, y = 70,anchor= "center")
loadBtn = tk.Button(page, text="Load file", command=loadFile)
loadBtn.place(relx=.5, y = 90,anchor= "e")

#A help button that explains how to use the program
def popUp(txt):
    popup = tk.Tk()
    popup.wm_title("Help")
    label = tk.Label(popup, text=txt)
    label.pack(side="top", fill="x", pady=10, padx=10)
    close = tk.Button(popup, text="OK", command = popup.destroy)
    close.pack()
txt = ("Welcome to this simple program made by Omar Shoura.\n " +
        "Chose a file and the program will try to predict what language it is\n" +
        "Current supported languages are: \n" + 
        "English, French, Dutch, German, Croatian, French, Romanian, Spanish")
helpBtn = tk.Button(page, text="Help", command=lambda: popUp(txt))
helpBtn.place(relx=.5, y = 90, anchor= "w")

resultsLbl = tk.Label(page, text=page.result, font=("Helvetica", 14))
resultsLbl.place(relx=.5, y = 115, anchor= "n")


page.geometry("400x200")
page.minsize(400, 200)
page.maxsize(400, 200)
page.title = "Language predictor"
page.mainloop()
