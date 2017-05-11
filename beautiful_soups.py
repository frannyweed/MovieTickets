from bs4 import BeautifulSoup
import urllib.request


#print(soup)
#based on the day, list movies, times, and prices

def soupy(url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")
    soup.prettify()

def get_dates():
    #return soupy("http://www.fandango.com/regalwebsterplace11_aaaxr/theaterpage")
    #soupy("http://www.fandango.com/regalwebsterplace11_aaaxr/theaterpage")
    url = "http://www.fandango.com/regalwebsterplace11_aaaxr/theaterpage"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")
    soup.prettify()

    #DATES
    dates = [x.text.strip() for x in soup.findAll("a", {"class": "date-area"})]
    dates = [x.replace('\n\n', ', ') for x in dates]
    dates = [x.replace('\n', ' ') for x in dates]
    dates = dates[:7]

    #URLS
    urls = [x.get('href') for x in soup.findAll("a", {"class": "date-area"})]
    urls = urls[:7]

    print(dates)
    print(urls)

def get_movies(url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")
    soup.prettify()
    movie_titles_list = [x.text.strip() for x in soup.findAll("a", {"class": "dark showtimes-movie-title"})]
    print(movie_titles_list)

def get_times(url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")
    soup.prettify()
    #times = [[y.findAll("time", {"class": "timeInfo"}] for y in
    times = [[z.text for z in y.findAll('time', {'class':'timeInfo'})] for y in [x for x in soup.findAll("div", {"class": "showtimes-times"})]]
    print(times)

if __name__ == "__main__":
    get_dates()
    get_movies("http://www.fandango.com/regalwebsterplace11_aaaxr/theaterpage?date=5/10/2017")
    get_times("http://www.fandango.com/regalwebsterplace11_aaaxr/theaterpage?date=5/10/2017")



