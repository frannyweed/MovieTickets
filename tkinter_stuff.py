'''
THIS IS SIMON'S (MASTER) DOCUMENT. DO NOT MAKE EDITS UNLESS YOU'VE BEEN CELARED TO
'''

from tkinter import *
from tkinter.font import *

from purchase import check_ticket
from beautiful_soups import get_dates
from beautiful_soups import get_movies
from beautiful_soups import get_times

class App():
    def __init__(self, master):
        self.master = master

        #lists
        self.day_list, self.date_url = get_dates()
        self.time_list = ["3:00pm", "5:00pm", "7:00pm", "9:00pm", "11:00pm"]

        #variables
        self.response = StringVar()
        self.response.set("sample")


        self.day_var = StringVar()
        self.movie_var = StringVar()
        self.time_var = StringVar()
        self.day_var.set(self.day_list[0])
        self.time_var.set("Select a time")

        self.movie_list = get_movies(self.date_url[self.day_list.index(self.day_var.get())])

        #self.movie_var.set(self.movie_list[0])
        self.movie_var.set("Select a movie")
        self.movie_var.set(self.movie_list[0])

        #labels
        self.title = Label(master, text="Movie Ticket App").grid(row=1,column=1,columnspan=3,sticky="e" + "w")
        self.ticket_label = Label(master, text="Tickets:").grid(row=4,column=1,sticky="e" + "w")
        self.cost_label = Label(master, text="Cost:").grid(row=4,column=3,sticky="e" + "w")
        self.result_label = Label(master, textvariable=self.response).grid(row=5, column=3, sticky="e" + "w")

        #listbox
        '''
        self.movie_listbox = Listbox(master, listvariable=self.movie_list,height=5)
        self.movie_listbox.grid(row=2,rowspan=2,column=2)
        '''

        #optionmenus
        self.date_menu = OptionMenu(master, self.day_var, *self.day_list, command=self.get_movie_list)
        self.date_menu.grid(row=2, column=1, sticky="e" + "w")

        self.time_list = ["Please Select a Movie First"]
        self.time_list = get_times(self.date_url[self.day_list.index(self.day_var.get())])

        self.movie_menu = OptionMenu(master, self.movie_var, *self.movie_list, command=self.get_time_list)
        self.movie_menu.grid(row=2,column=2,sticky="e" + "w")

        self.time_menu = OptionMenu(master, self.time_var, *self.time_list[0])
        self.time_menu.grid(row=2, column=3, sticky="e" + "w")

        #spinboxes
        self.ticket_amount = Spinbox(values=(1,2,3,4,5,6,7,8,9,10,11,12))
        self.ticket_amount.grid(row=4,column=2,sticky="e" + "w")

        #button
        self.purchase_button = Button(master, text="Purchase", command=lambda:self.response.set(check_ticket()(self.day_var.get(),self.movie_var.get(),self.time_var.get(),self.ticket_amount.get()))).grid(row=5,column=2,sticky="e" + "w")

    def get_movie_list(self, value):
        self.movie_list = get_movies(self.date_url[self.day_list.index(self.day_var.get())])
        self.movie_menu.destroy()
        self.movie_menu = OptionMenu(self.master, self.movie_var, *self.movie_list, command=self.get_time_list)
        self.movie_menu.grid(row=2, column=2, sticky="e" + "w")


    def get_time_list(self, value):
        self.time_list = get_times(self.date_url[self.day_list.index(self.day_var.get())])
        self.time_menu.destroy()
        self.time_menu = OptionMenu(self.master, self.time_var, *self.time_list[self.movie_list.index(self.movie_var.get())])
        self.time_menu.grid(row=2, column=3, sticky="e" + "w")

if __name__ == "__main__":
    root = Tk()
    root.title("Movie Ticket App")
    my_app = App(root)
    root.mainloop()