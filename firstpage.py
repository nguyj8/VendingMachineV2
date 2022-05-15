from tkinter import *
# from tkinter import font as tkfont

import tkinter as tk


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Snacks", font=('Karma', 25, 'bold'), foreground="#F25757",
                         background="#083D77", bd=10, relief=RAISED)

        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Return", command=lambda: controller.show_frame("StartPage"))
        button.pack()
