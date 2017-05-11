'''
from tkinter import *
class Ticket():
    def __init__(self,master):
        self.title_font = font.Font(family = "Courier New")
        self.title = Label(master, text = "Your ticket", fg = "dark blue")
        self.title.grid(column=0,row=0)


if __name__ == "__main__":
    root = Tk()
    root.title("Your Ticket")
    my_app = Ticket(root)
    root.mainloop()
'''
from bs4 import BeautifulSoup
import webbrowser
import os
from urllib.request import pathname2url

soup = BeautifulSoup("<html>", 'lxml') # make soup object with html tag only

main_tag = soup.html # grab the html tag so we can add to it

body_tag = soup.new_tag('body')
main_tag.append(body_tag)

#myDIV
new_tag = soup.new_tag("style")
new_tag.string = "#mount{width: 304px; height: 228px; img src: movie.png; img alt: Mountain View}"
main_tag.append(new_tag)
'''
mountain = soup.new_tag("img", id = "mount")
body_tag.append(mountain)
'''

mountain = soup.new_tag("h2", id = "mount")


style_tag = soup.new_tag("style")
style_tag.string = '#myDIV{line-height: 20%;font-family: arial-black; color:black;text-align:center;}'
main_tag.append(style_tag)
back = soup.new_tag("h4", id = "myDIV")
back.string = "Regal Webster Theater"
body_tag.append(back)

#PRESENTING
style_tag2 = soup.new_tag('style')
style_tag2.string = '#presenting{font-family: arial-black;color:black;line-height: 0%; text-align:center;font-style: italic;}'

main_tag.append(style_tag2)

new2 = soup.new_tag("h5", id="presenting")
new2.string = "Presenting"
body_tag.append(new2)

#MOVIE

style_tag3 = soup.new_tag("style")
style_tag3.string = "#movie{line-height:0% height:40px;color: red; text-align:center;animation: mymove 5s infinite} @keyframes mymove{50% {color: purple;}}"
main_tag.append(style_tag3)

new3 = soup.new_tag('h1', id='movie')
new3.string = "Beauty and The Beast"
body_tag.append(new3)

#TIME

style_tag4 = soup.new_tag('style')
style_tag4.string= "#time{column=2; font-family: Lucida Console;"
main_tag.append(style_tag4)

new4 = soup.new_tag("h4", id = "#time")
new4.string = "1:00 pm Sat 10/13/16"
body_tag.append(new4)


file_name = "ticket.html"

with open(file_name, 'w') as file:
    for line in soup:
        file.write(str(line))

print(soup.prettify())
file_name = 'file:{}'.format(pathname2url(os.path.abspath(file_name)))
webbrowser.open_new(file_name) # opens in default browser