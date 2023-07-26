import tkinter as tk
# from tkinter.font import NORMAL, ROMAN, BOLD, ITALIC, nametofont, Font, families, names

class PeterAlert:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("120x180")
        self.root.attributes("-toolwindow", True)
        self.root.attributes("-topmost", True)
        self.root.title("Peter Alert")
        photo = tk.PhotoImage(file="peterface.png", height=150, width=90)
        tk.Label(self.root, image=photo).pack(side='top', fill="x")
        tk.Button(self.root, text="OK", command=self.root.destroy, font=("Segoe UI", 10)).pack(ipadx=40, padx=10, pady=2, side='bottom')
        self.root.mainloop()

# PeterAler()