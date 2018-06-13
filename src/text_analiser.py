from ui.MainWindow import UI


# classifiersDictionary = {'MLP': 1, 'NaiveBayes': 2, 'NearestNeighbors': 3, 'SVM': 4}
classifiersDictionary = {
    'MLP': 1,
    'NearestNeighbors': 2,
    'SVM': 3
}
userInterface = UI(classifiersDictionary)
userInterface.mainWindow.mainloop()
