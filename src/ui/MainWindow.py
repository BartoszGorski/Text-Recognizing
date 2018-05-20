import tkinter
#from src.Interfaces.ClassificationModule import ClassificationModule
#from src.Classifiers.MLPClassifier import *
#from src.Classifiers.NaiveBayesClassifier import *
#from src.Classifiers.NearestNeighborsClassifier import *
#from src.Classifiers.SupportVectorMachineClassifier import *


class UI:
    def __init__(self, classifiersDict = dict()):
        self.modulesDictionary = dict()
        self.mainWindow = tkinter.Tk()
        self.mainWindow.geometry("600x440")
        self.initManagementFrame(classifiersDict)
        self.initClassificationFrame()
        self.initMainLayout()


    def initMainLayout(self):
        self.managementLabel.grid(column = 0, row = 0)
        self.managementFrame.grid(column = 0, row = 1, padx = 30, sticky = tkinter.W + tkinter.E + tkinter.N + tkinter.S)
        self.classificationLabel.grid(column = 1, row = 0)
        self.classificationFrame.grid(column = 1, row = 1, sticky = tkinter.W + tkinter.E + tkinter.N + tkinter.S)


    def initManagementFrameLayout(self):
        self.classifierTypeLabel.pack(pady = (30, 0))
        self.classifierTypeListbox.pack(padx = 30, pady = (0, 30))
        self.createTextBoxLabel.pack()
        self.createTextBox.pack()
        self.createButton.pack(pady = (5, 30))


    def initClassificationFrameLayout(self):
        self.classifierLabel.pack(pady = (30, 0))
        self.classifierListbox.pack(padx = 30)
        self.removeButton.pack(pady = (5, 25))
        self.classifyTextBoxLabel.pack()
        self.classifyTextBox.pack(padx = 15)
        self.classifyButton.pack(pady = (5, 0))
        self.scoreLabel.pack(pady = (5, 30))


    def initClassificationFrame(self):
        self.classificationFrame = tkinter.Frame(self.mainWindow, width=500, height=400, bd=2, borderwidth=2, relief=tkinter.GROOVE)
        self.classificationLabel = tkinter.Label(self.mainWindow, text = "Klasyfikacja")
        self.classifierListbox = tkinter.Listbox(self.classificationFrame)
        self.classifierLabel = tkinter.Label(self.classificationFrame, text = "Moduły klasyfikujące")
        self.classifyButton = tkinter.Button(self.classificationFrame, text = "Klasyfikuj")
        self.classifyTextBox = tkinter.Entry(self.classificationFrame, width = 50)
        self.classifyTextBoxLabel = tkinter.Label(self.classificationFrame, text = "Tekst do klasyfikacji")
        self.removeButton = tkinter.Button(self.classificationFrame, text = "Usuń moduł")
        self.scoreLabel = tkinter.Label(self.classificationFrame, text = "Wynik klasyfikacji: ")
        self.initClassificationFrameLayout()

        self.removeButton.bind("<Button-1>", self.onClickRemoveButton)
        self.classifyButton.bind("<Button-1>", self.onClickClassifyButton)


    def initManagementFrame(self, classifiersDict = dict()):
        self.managementFrame = tkinter.Frame(self.mainWindow, width=500, height=400, bd=2, borderwidth=2, relief=tkinter.GROOVE)
        self.managementLabel = tkinter.Label(self.mainWindow, text = "Tworzenie modułów")
        self.classifierTypeListbox = tkinter.Listbox(self.managementFrame)
        self.setClassifierTypeListboxElements(classifiersDict)
        self.classifierTypeListbox.select_set(0)
        self.classifierTypeLabel = tkinter.Label(self.managementFrame, text = "Typy algorytmów")
        self.createButton = tkinter.Button(self.managementFrame, text = "Stwórz")
        self.createTextBox = tkinter.Entry(self.managementFrame)
        self.createTextBoxLabel = tkinter.Label(self.managementFrame, text = "Nazwa nowego modułu")
        self.initManagementFrameLayout()

        self.createButton.bind("<Button-1>", self.onClickCreateButton)


    def setClassifierTypeListboxElements(self, elements = dict()):
        self.classifierTypeListbox.delete(0, tkinter.END)
        for element in elements:
            self.classifierTypeListbox.insert(tkinter.END, element)


    def setClassifierListboxElements(self, elements = dict()):
        self.classifierListbox.delete(0, tkinter.END)
        for element in elements:
            self.classifierListbox.insert(tkinter.END, element)

    
    def onClickCreateButton(self, event):
        classifierTypeSelected = self.classifierTypeListbox.get(self.classifierTypeListbox.curselection())
        moduleName = self.createTextBox.get()
        self.createTextBox.delete(0, tkinter.END)

        self.modulesDictionary[moduleName] = 1 #create proper classifier via dictionary, for example: MLPClassifier
        self.setClassifierListboxElements(self.modulesDictionary)


    def onClickRemoveButton(self, event):
        moduleSelected = self.classifierListbox.get(self.classifierListbox.curselection())
        self.modulesDictionary.pop(moduleSelected)
        self.setClassifierListboxElements(self.modulesDictionary)


    def onClickClassifyButton(self, event):
        moduleSelected = self.classifierListbox.get(self.classifierListbox.curselection())
        textToClassify = self.classifyTextBox.get()
        #predictionResult = self.modulesDictionary[moduleSelected].predict(textToClassify) #send features container as parameter
        scoreLabelNewText = self.scoreLabel.cget("text") + "PREDICTION RESULT" #add predicitionResult here
        self.scoreLabel.config(text = scoreLabelNewText)




#classifiersDictionary = {'MLP': MLPClassifier, 'Naive Bayes': NaiveBayesClassifier, 'Nearest Neighbors': NearestNeighborsClassifier, 'SVM': SupportVectorMachineClassifier}
classifiersDictionary = {'MLP': 1, 'Naive Bayes': 2, 'Nearest Neighbors': 3, 'SVM': 4}
userInterface = UI(classifiersDictionary)
userInterface.mainWindow.mainloop()