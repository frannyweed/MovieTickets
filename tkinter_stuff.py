'''
THIS IS SIMON'S (MASTER) DOCUMENT. DO NOT MAKE EDITS UNLESS YOU'VE BEEN CELARED TO
'''

from tkinter import *
from tkinter.font import *

class App():
    def __init__(self, master):
        #variables

        #labels
        self.title = Label(master, text="Movie Ticket App").grid(row=1,column=1,columnspan=3,sticky="e" + "w")
        self.ticket_label = Label(master, text="Tickets:").grid(row=4,column=1,sticky="e" + "w")
        self.cost_label = Label(master, text="Cost:").grid(row=4,column=3,sticky="e" + "w")

        #dropdowns

        #buttons
        self.purchase_button = Button(master, text="Purchase").grid(row=5,column=2,sticky="e" + "w")

        #spinboxes
        self.ticket_amount = Spinbox(master, from_=0, to=8, increment=1).grid(row=4,column=2,sticky="e" + "w")


if __name__ == "__main__":
    root = Tk()
    root.title("Movie Ticket App")
    my_app = App(root)
    root.mainloop()