import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=720
        height=478
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_178=tk.Button(root)
        GButton_178["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_178["font"] = ft
        GButton_178["fg"] = "#000000"
        GButton_178["justify"] = "center"
        GButton_178["text"] = "Klick mich"
        GButton_178.place(x=410,y=130,width=140,height=56)
        GButton_178["command"] = self.GButton_178_command

        GCheckBox_366=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_366["font"] = ft
        GCheckBox_366["fg"] = "#333333"
        GCheckBox_366["justify"] = "center"
        GCheckBox_366["text"] = "CheckBox"
        GCheckBox_366.place(x=370,y=180,width=164,height=68)
        GCheckBox_366["offvalue"] = "0"
        GCheckBox_366["onvalue"] = "1"
        GCheckBox_366["command"] = self.GCheckBox_366_command

        GCheckBox_764=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_764["font"] = ft
        GCheckBox_764["fg"] = "#333333"
        GCheckBox_764["justify"] = "center"
        GCheckBox_764["text"] = "CheckBox"
        GCheckBox_764.place(x=420,y=240,width=70,height=25)
        GCheckBox_764["offvalue"] = "0"
        GCheckBox_764["onvalue"] = "1"
        GCheckBox_764["command"] = self.GCheckBox_764_command

        GLineEdit_204=tk.Entry(root)
        GLineEdit_204["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_204["font"] = ft
        GLineEdit_204["fg"] = "#333333"
        GLineEdit_204["justify"] = "center"
        GLineEdit_204["text"] = "Entry"
        GLineEdit_204.place(x=50,y=60,width=166,height=104)

        GLabel_148=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_148["font"] = ft
        GLabel_148["fg"] = "#333333"
        GLabel_148["justify"] = "center"
        GLabel_148["text"] = "label"
        GLabel_148.place(x=330,y=30,width=70,height=25)

    def GButton_178_command(self):
        print("command")


    def GCheckBox_366_command(self):
        print("command")


    def GCheckBox_764_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
