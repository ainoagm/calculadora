from tkinter import *
from tkinter import ttk 

import calculator

def imprimeuno():
    print(1)

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("272x300")
        self.title("Calculadora")

        s = ttk.Style()
        s.theme_use('alt')
        # s.configure('my.TLabel', font='Helvetica 36', background='black', foreground='white')


        self.display = ttk.Label(self, text='9', anchor='e', background='black', foreground='white', font='Helvetica 36')
        self.display.grid(column=0, row=0, columnspan=2)

        self.calcButtonC = ttk.Frame(self, width=136, height=50)
        btn = ttk.Button(self.calcButtonC, text='C')
        self.calcButtonC.pack_propagate(False)
        btn.pack(side=TOP, fill=BOTH, expand=True)
        self.calcButtonC.grid(column=0, row=1, columnspan=2)

        self.calcButtonCs = ttk.Frame(self, width=68, height=50)
        btn = ttk.Button(self.calcButtonCs, text='+/-')
        self.calcButtonCs.pack_propagate(False)
        btn.pack(side=TOP, fill=BOTH, expand=True)
        self.calcButtonCs.grid(column=2, row=1)

        self.calcButtondiv = ttk.Frame(self, width=68, height=50)
        btn = ttk.Button(self.calcButtondiv, text='/')
        self.calcButtondiv.pack_propagate(False)
        btn.pack(side=TOP, fill=BOTH, expand=True)
        self.calcButtondiv.grid(column=3, row=1)

        # self.botonC= ttk.Button(self, text='C')
        # self.botonC.pack(side=TOP, fill=BOTH)



if __name__ == "__main__":
    app = MainApp ()
    app.mainloop()

    