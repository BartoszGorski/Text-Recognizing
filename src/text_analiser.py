from ui.MainWindow import UI


classifiersDictionary = {'MLP': 1, 'NaiveBayes': 2, 'NearestNeighbors': 3, 'SVM': 4}
userInterface = UI(classifiersDictionary)
userInterface.mainWindow.mainloop()
