import tkinter


class DialogWindow:
    def __init__(self, parent, minLength = 0, txt = ""):
        top = self.top = tkinter.Toplevel(parent)

        if len(txt) < 1:
            tkinter.Label(top, text="Minimalna długość tekstu wynosi " + str(minLength) + " znaków!").pack()
        else:
            tkinter.Label(top, text=txt).pack()

        okButton = tkinter.Button(top, text="OK", command=self.ok)
        okButton.pack(pady=5)

    def ok(self):
        self.top.destroy()
