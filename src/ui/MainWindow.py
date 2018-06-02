import tkinter
from ui.DialogWindow import DialogWindow

from Interfaces.ClassificationModule import ClassificationModule, LanguageType
from utils.FeaturesGen import FeaturesGen


class UI:
    def __init__(self, classifiersDict=dict()):
        self.modulesDictionary = dict()
        self.loadClassifiers()
        self.mainWindow = tkinter.Tk()
        self.initManagementFrame(classifiersDict)
        self.initClassificationFrame()
        self.initMainLayout()
        self.minLength = 30;
        self.featuresGenerator = FeaturesGen()

    def loadClassifiers(self):
        self.modulesDictionary = {
            'MLP': ClassificationModule.load_classifier('../classifiers_pkl/MLP.pkl'),
            'NaiveBayes': ClassificationModule.load_classifier(
                '../classifiers_pkl/NaiveBayes.pkl'),
            'NearestNeighbors': ClassificationModule.load_classifier(
                '../classifiers_pkl/NearestNeighbors.pkl'),
            'SVM': ClassificationModule.load_classifier('../classifiers_pkl/SVM.pkl')
        }

    def initMainLayout(self):
        #self.managementLabel.grid(column=0, row=0)
        #self.managementFrame.grid(column=0, row=1,
                                  #sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)
        self.classificationLabel.grid(column=0, row=0)
        self.classificationFrame.grid(column=0, row=1,
                                      sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)

    def initManagementFrameLayout(self):
        self.classifierTypeLabel.pack(pady=(30, 0))
        self.classifierTypeListbox.pack(padx=30, pady=(0, 30))
        self.createTextBoxLabel.pack()
        self.createTextBox.pack()
        self.createButton.pack(pady=(5, 30))

    def initClassificationFrameLayout(self):
        self.classifierLabel.pack(pady=(30, 0))
        self.classifierListbox.pack(padx=30)
        #self.removeButton.pack(pady=(5, 25))
        self.classifyTextBoxLabel.pack(pady=(15,0))
        self.classifyTextBox.pack(padx=15)
        self.classifyButton.pack(pady=(5, 0))
        self.scoreLabel.pack(pady=(5, 30))

    def initClassificationFrame(self):
        self.classificationFrame = tkinter.Frame(self.mainWindow, width=500, height=400,
                                                 bd=2, borderwidth=2,
                                                 relief=tkinter.GROOVE)
        self.classificationLabel = tkinter.Label(self.mainWindow, text="Klasyfikacja")
        self.classifierListbox = tkinter.Listbox(self.classificationFrame)
        self.setClassifierListboxElements(self.modulesDictionary)
        self.classifierLabel = tkinter.Label(self.classificationFrame,
                                             text="Moduły klasyfikujące")
        self.classifyButton = tkinter.Button(self.classificationFrame, text="Klasyfikuj")
        #self.classifyTextBox = tkinter.Entry(self.classificationFrame, width=50, validate="all",
        #                                     validatecommand=self.validateLength, highlightthickness=1)
        self.classifyTextBox = tkinter.Text(self.classificationFrame, width=50, height=5)

        self.classifyTextBoxLabel = tkinter.Label(self.classificationFrame,
                                                  text="Tekst do klasyfikacji")
        self.removeButton = tkinter.Button(self.classificationFrame, text="Usuń moduł")
        self.scoreLabel = tkinter.Label(self.classificationFrame,
                                        text="Wynik klasyfikacji: ")
        self.initClassificationFrameLayout()

        self.removeButton.bind("<Button-1>", self.onClickRemoveButton)
        self.classifyButton.bind("<Button-1>", self.onClickClassifyButton)
        self.classifyTextBox.bind('<<Modified>>', self.validateLength)

    def initManagementFrame(self, classifiersDict=dict()):
        self.managementFrame = tkinter.Frame(self.mainWindow, width=500, height=400, bd=2,
                                             borderwidth=2, relief=tkinter.GROOVE)
        self.managementLabel = tkinter.Label(self.mainWindow, text="Tworzenie modułów")
        self.classifierTypeListbox = tkinter.Listbox(self.managementFrame)
        self.setClassifierTypeListboxElements(classifiersDict)
        self.classifierTypeListbox.select_set(0)
        self.classifierTypeLabel = tkinter.Label(self.managementFrame,
                                                 text="Typy algorytmów")
        self.createButton = tkinter.Button(self.managementFrame, text="Stwórz")
        self.createTextBox = tkinter.Entry(self.managementFrame)
        self.createTextBoxLabel = tkinter.Label(self.managementFrame,
                                                text="Nazwa nowego modułu")
        self.initManagementFrameLayout()

        self.createButton.bind("<Button-1>", self.onClickCreateButton)

    def setClassifierTypeListboxElements(self, elements=dict()):
        self.classifierTypeListbox.delete(0, tkinter.END)
        for element in elements:
            self.classifierTypeListbox.insert(tkinter.END, element)

    def setClassifierListboxElements(self, elements=dict()):
        self.classifierListbox.delete(0, tkinter.END)
        for element in elements:
            self.classifierListbox.insert(tkinter.END, element)

    def onClickCreateButton(self, event):
        classifierTypeSelected = self.classifierTypeListbox.get(
            self.classifierTypeListbox.curselection())
        moduleName = self.createTextBox.get()
        self.createTextBox.delete(0, tkinter.END)
        self.modulesDictionary[moduleName] = self.classifiers[classifierTypeSelected]
        self.setClassifierListboxElements(self.modulesDictionary)

    def onClickRemoveButton(self, event):
        moduleSelected = self.classifierListbox.get(self.classifierListbox.curselection())
        self.modulesDictionary.pop(moduleSelected)
        self.setClassifierListboxElements(self.modulesDictionary)

    def onClickClassifyButton(self, event):
        if not self.classifierListbox.curselection():
            DialogWindow(self.mainWindow, txt="Wybierz moduł klasyfikacyjny z listy!")
        elif len(self.classifyTextBox.get("1.0", tkinter.END)) < self.minLength:
            DialogWindow(self.mainWindow, self.minLength)
        else:
            moduleSelected = self.classifierListbox.get(self.classifierListbox.curselection())
            textToClassify = self.classifyTextBox.get("1.0", tkinter.END)
            analysedText = self.featuresGenerator.analyse_text(textToClassify)[1:]
            predictionResult = self.modulesDictionary[moduleSelected].predict([analysedText])
            scoreLabelNewText = self.createClassifyResultText(predictionResult)
            self.scoreLabel.config(text=scoreLabelNewText)

    def validateLength(self, event=None):
        currentLength = len(self.classifyTextBox.get("1.0", tkinter.END))
        self.classifyTextBox.edit_modified(False)

        if currentLength >= self.minLength:
            self.classifyTextBox.config(fg="green")
        else:
            self.classifyTextBox.config(fg="red")
        return True

    def createClassifyResultText(self, predictionResult):
        resultName = LanguageType(predictionResult).name
        if resultName == "garbage" or resultName == "code" or resultName == "random":
            languageType = "język nienaturalny"
        elif resultName == "polish":
            languageType = "język polski"
        else:
            languageType = "język angielski"
        return "Wynik klasyfikacji: {}".format(languageType)

