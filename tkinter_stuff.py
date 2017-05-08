'''
THIS IS SIMON'S (MASTER) DOCUMENT. DO NOT MAKE EDITS UNLESS YOU'VE BEEN CELARED TO
'''

from tkinter import *
from tkinter.font import *
'''
from purchase import Records
'''
class App():
    def __init__(self, master):
        #lists
        self.day_list = []
        for i in range(31):
            self.day_list.append(i+1)
        self.month_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
        self.time_list = ["3:00pm", "5:00pm", "7:00pm", "9:00pm", "11:00pm"]
        self.attempt_movie_list = ["Star Wars", "Hunger games or something", "yee", "A super long title to test out the app"]

        #variables
        self.response = StringVar()
        self.response.set("sample")

        self.movie_list = StringVar()
        self.movie_list.set("memes\ and\ dreams")
        self.movie_list.get()
        #self.movie_list.set("Star Wars", "Hunger games or something", "yee", "A super long title to test out the app")

        self.day_var = StringVar()
        self.month_var = StringVar()
        self.time_var = StringVar()
        self.day_var.set("Select a day")
        self.month_var.set("Select a month")
        self.time_var.set("Select a time")

        #labels
        self.title = Label(master, text="Movie Ticket App").grid(row=1,column=1,columnspan=3,sticky="e" + "w")
        self.ticket_label = Label(master, text="Tickets:").grid(row=4,column=1,sticky="e" + "w")
        self.cost_label = Label(master, text="Cost:").grid(row=4,column=3,sticky="e" + "w")
        self.result_label = Label(master, textvariable=self.response).grid(row=5, column=3, sticky="e" + "w")

        #listbox
        self.movie_listbox = Listbox(master, listvariable=self.movie_list,heigh=5).grid(row=2,rowspan=2,column=2)

        #optionmenus
        self.day_menu = OptionMenu(master, self.day_var, *self.day_list).grid(row=2, column=1,sticky="e" + "w")
        self.month_menu = OptionMenu(master, self.month_var, *self.month_list).grid(row=3, column=1,sticky="e" + "w")
        self.time_menu = OptionMenu(master, self.time_var, *self.time_list).grid(row=2, column=3, sticky="e" + "w")

        #buttons
        self.purchase_button = Button(master, text="Purchase", command=lambda:self.response.set(self.Response())).grid(row=5,column=2,sticky="e" + "w")

        #spinboxes
        self.ticket_amount = Spinbox(master, from_=0, to=12, increment=1).grid(row=4,column=2,sticky="e" + "w")


if __name__ == "__main__":
    root = Tk()
    root.title("Movie Ticket App")
    my_app = App(root)
    root.mainloop()