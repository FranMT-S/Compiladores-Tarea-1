from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile
from ..core.core import *

class Gui:
   
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Buscador De Patrones")
        self.root.geometry("500x300")
        self.root.eval('tk::PlaceWindow . center')
        self.labelNum = StringVar()
        self.labelNumAndLetters = StringVar()
        self.labelThreeVowels = StringVar()
        self.labelSpecialCharacters = StringVar()
        
        self.btn = Button(self.root, text ='Buscar Archivo', command = lambda:self.open_file())
        self.btn.pack(side = TOP, pady = 10)

        self.LabelFrame = Frame(self.root)
        self.LabelFrame.pack(fill = BOTH)

        Label(self.LabelFrame,text="Numeros:").grid(row=0, column=0,sticky=E)
        Label(self.LabelFrame,text="Numeros Y Letras:").grid(row=1, column=0,sticky=E)
        Label(self.LabelFrame,text="Tres Vocales:").grid(row=2, column=0,sticky=E)
        Label(self.LabelFrame,text="Caracteres Especiales:").grid(row=3, column=0,sticky=E)

        Label( self.LabelFrame, textvariable=self.labelNum ).grid(row=0, column=1, sticky=W)
        Label( self.LabelFrame, textvariable=self.labelNumAndLetters ).grid(row=1, column=1, sticky=W)
        Label( self.LabelFrame, textvariable=self.labelThreeVowels ).grid(row=2, column=1, sticky=W)
        Label( self.LabelFrame, textvariable=self.labelSpecialCharacters ).grid(row=3, column=1, sticky=W)
       

  
   

    def open_file(self): 
        with askopenfile(mode ='r', filetypes =[('Python Files', '*.txt'),('All Files', '*.*')]) as file:
            content = file.read()
            self.labelNum.set(str(find_sequence_of_numbers(content)))
            self.labelNumAndLetters.set(str(find_sequence_numbers_and_letters(content)))
            self.labelThreeVowels.set(str(find_three_repeated_vowels(content)))
            self.labelSpecialCharacters.set(str(find_special_character(content)))
                
            with open("patrones encontrados.txt", "w") as found:
                found.write("Numeros: " + self.labelNum.get() + "\n")
                found.write("Numeros Y Letras: " +self.labelNumAndLetters.get() + "\n")
                found.write("Tres Vocales: " +self.labelThreeVowels.get() + "\n")
                found.write("Caracteres Especiales: " +self.labelSpecialCharacters.get() + "\n")


    def Draw(self):
        mainloop()

# This function will be used to open
# file in read mode and only Python files
# will be opened
