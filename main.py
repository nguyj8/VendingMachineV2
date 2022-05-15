from tkinter import *
from PIL import ImageTk, Image
from tkinter import font as tkfont
from firstpage import PageOne
from secondpage import PageTwo

import tkinter as tk


class Root(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family="Karma", size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):  # Welcome page, Snacks page, Drinks page
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsnew")  # Stick to every side
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        f1 = Frame(relief=RAISED, bd=50, bg="#083D77")
        f1.pack(padx=15, pady=15)

        label = tk.Label(self, text="EZQuik", font=("Karma", 25, "bold"), foreground="#F25757", background="#083D77",
                         bd=10, relief=RAISED)
        label.pack(side="top", fill='x', pady=10)
        label1 = tk.Label(self, text="Satisfy Your Cravings", font=("Karma", 16),
                          foreground="#000000")
        label1.pack(padx=50, pady=15)

        password_label = tk.Label(self, text="Password", font=("Karma", 14), foreground="#000000")
        password_label.pack(pady=10)

        password = tk.StringVar()
        password_entry = tk.Entry(self, textvariable=password, font=("Karma", 12), width=20, relief=RAISED)
        password_entry.focus_set()  # Enables blinker in entry box
        password_entry.pack(ipady=7)

        def handle(_):
            password_entry.configure(foreground="#000000", show='*')  # Encrypts password input

        password_entry.bind("<FocusIn>", handle)

        def password_check():  # Enter Password prior to usage
            if password.get() == "123":
                controller.show_frame("PageOne")
            else:
                incorrect_password["text"] = "Incorrect Password"

        enter_button = tk.Button(self, text="Enter", font=("Karma", 12, "bold"), foreground="#F25757",
                                 command=password_check)
        enter_button.pack(pady=10)

        incorrect_password = tk.Label(self, text="", font=("Karma", 12), foreground="#F25757",
                                      background="#083D77", padx=50, bd=15, relief=RAISED)
        incorrect_password.pack(fill="both", expand=True)

        def close():  # Quit button
            self.destroy()
            self.quit()

        Button(self, text="Quit", font=("Karma", 12, "bold"), foreground="#F25757", command=close).pack(pady=30)

        bottom_frame = tk.Frame(self, relief=RAISED, borderwidth=2)
        bottom_frame.pack(fill='x', side="bottom")

        # visa = tk.PhotoImage(file="visa.png")
        # visa_label = tk.Label(bottom_frame, image=visa)
        # visa_label.pack(side=LEFT)
        # visa_label.image = visa


if __name__ == "__main__":
    root = Root()
    root.geometry("800x600")
    root.mainloop()
