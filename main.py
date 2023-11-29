import tkinter as tk

class MyCalculator02:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("300x300")
        self.root.title("My Calculator")
        self.label = tk.Label(self.root, text="Hello tiggaQ 01", font=('Arial', 20))
        self.label.pack()
        
        self.button = tk.Button(self.root, text="CLick here")
        self.button.place(x=20 , y=50)

        self.root.mainloop()
MyCalculator02()