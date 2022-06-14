from tkinter import *

root = Tk()
root.title("Calculator")

def myClick():
    myLabel = Label(root, text="Look I clicked a Button!!!")
    myLabel.pack()

buttonWidth=25
buttonHeight=20

TextField = Entry(root)
TextField.grid(column=0,columnspan=4, row=0, ipadx=buttonWidth*4, ipady=buttonHeight,padx=1, pady=1, sticky=W)

ButtonOne = Button(root, text="1", padx=buttonWidth, pady=buttonHeight, command=myClick, bg="grey")
ButtonOne.grid(column=0, row=1, padx=1, pady=1, sticky=W)
ButtonTwo = Button(root, text="2", padx=buttonWidth, pady=buttonHeight, command=myClick, bg="grey")
ButtonTwo.grid(column=1, row=1, padx=1, pady=1, sticky=W)
ButtonThree = Button(root, text="3", padx=buttonWidth, pady=buttonHeight, command=myClick, bg="grey")
ButtonThree.grid(column=2, row=1, padx=1, pady=1, sticky=W)

ButtonFour = Button(root, text="4", padx=buttonWidth, pady=buttonHeight, command=myClick, bg="grey")
ButtonFour.grid(column=0, row=2, padx=1, pady=1, sticky=W)
ButtonFive = Button(root, text="5", padx=buttonWidth, pady=buttonHeight, command=myClick, bg="grey")
ButtonFive.grid(column=1, row=2, padx=1, pady=1, sticky=W)
ButtonSix = Button(root, text="6", padx=buttonWidth, pady=buttonHeight, command=myClick, bg="grey")
ButtonSix.grid(column=2, row=2, padx=1, pady=1, sticky=W)

ButtonSeven = Button(root, text="7", padx=buttonWidth, pady=buttonHeight, command=myClick, bg="grey")
ButtonSeven.grid(column=0, row=3, padx=1, pady=1, sticky=W)
ButtonEight = Button(root, text="8", padx=buttonWidth, pady=buttonHeight, command=myClick, bg="grey")
ButtonEight.grid(column=1, row=3, padx=1, pady=1, sticky=W)
ButtonNine = Button(root, text="9", padx=buttonWidth, pady=buttonHeight, command=myClick, bg="grey")
ButtonNine.grid(column=2, row=3, padx=1, pady=1, sticky=W)


ButtonAdd = Button(root, text="+", padx=buttonWidth, pady=buttonHeight, command=myClick, bg="grey")
ButtonAdd.grid(column=3, row=1, padx=1, pady=1, sticky=W)
ButtonSub = Button(root, text="-", padx=buttonWidth, pady=buttonHeight, command=myClick, bg="grey")
ButtonSub.grid(column=3, row=2, padx=1, pady=1, sticky=W)
ButtonMul = Button(root, text="*", padx=buttonWidth, pady=buttonHeight, command=myClick, bg="grey")
ButtonMul.grid(column=3, row=3, padx=1, pady=1, sticky=W)
ButtonDiv = Button(root, text="/", padx=buttonWidth, pady=buttonHeight, command=myClick, bg="grey")
ButtonDiv.grid(column=3, row=4, padx=1, pady=1, sticky=W)
ButtonDel = Button(root, text="C", padx=buttonWidth, pady=buttonHeight, command=myClick, bg="grey")
ButtonDel.grid(column=2, row=4, padx=1, pady=1, sticky=W)
ButtonEquals = Button(root, text="=", padx=buttonWidth*3, pady=buttonHeight, command=myClick, bg="grey")
ButtonEquals.grid(column=0,columnspan=2, row=4, padx=1, pady=1, sticky=W)


root.mainloop()