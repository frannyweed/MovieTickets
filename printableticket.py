from bs4 import BeautifulSoup
import webbrowser
import os
from urllib.request import pathname2url
soup = BeautifulSoup("<html>", 'lxml') # make soup object with html tag only

main_tag = soup.html # grab the html tag so we can add to it

body_tag = soup.new_tag('body')
main_tag.append(body_tag)

#myDIV
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
style_tag4.string= "#time{font-family: Lucida Console;font-size:10;}"
main_tag.append(style_tag4)

new4 = soup.new_tag("h1", id = "#time")
new4.string = "1:00 pm Sat 10/13/16"
body_tag.append(new4)

#TICKETS + TICKET PRICE
style_tag5 = soup.new_tag("style")
style_tag5.string = "#ticket{font-family: Lucida Console;font-size:200;line-height: 0%;}"
main_tag.append(style_tag5)

new5 = soup.new_tag("h6", id = "#ticket")
new5.string = "5 tickets"
body_tag.append(new5)

#REGAL WEBSTER THEATERS

new_tag = soup.new_tag("style")
new_tag.string = "#mov{text-align: center;width: 300px}"
new_tag.center = "{text-align: center;}"
main_tag.append(new_tag)
regal = soup.new_tag("img", id = "mov", src = "movie.png", align = "right")
body_tag.append(regal)

file_name = "ticket.html"

with open(file_name, 'w') as file:
    for line in soup:
        file.write(str(line))

print(soup.prettify())
file_name = 'file:{}'.format(pathname2url(os.path.abspath(file_name)))
webbrowser.open_new(file_name) # opens in default browser