'''
Author: Nina Sachs 
'''

from bs4 import BeautifulSoup
import urllib.request


def soupy(url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")
    soup.prettify()
    return soup

def get_dates(url):
    url = "http://www.fandango.com/regalwebsterplace11_aaaxr/theaterpage"
    soup = soupy(url)

    #DATES
    dates = [x.text.strip() for x in soup.findAll("a", {"class": "date-area"})]
    dates = [x.replace('\n\n', ', ') for x in dates]
    dates = [x.replace('\n', ' ') for x in dates]
    dates = dates[:7]

    #URLS
    urls = [x.get('href') for x in soup.findAll("a", {"class": "date-area"})]
    urls = urls[:7]

    return dates, urls


def get_movies(url):
    soup = soupy(url)

    movie_titles_list = [x.text.strip() for x in soup.findAll("a", {"class": "dark showtimes-movie-title"})]
    movie_titles_list = [x.replace('  ', '\ ') for x in movie_titles_list]

    print(movie_titles_list)
    return movie_titles_list

def get_times(url):
    soup = soupy(url)

    times = [[z.text for z in y.findAll('time', {'class':'timeInfo'})] for y in [x for x in soup.findAll("div", {"class": "showtimes-times"})]]

    return times

if __name__ == "__main__":
    get_dates("http://www.fandango.com/regalwebsterplace11_aaaxr/theaterpage")
    get_movies("http://www.fandango.com/regalwebsterplace11_aaaxr/theaterpage?date=5/10/2017")
    get_times("http://www.fandango.com/regalwebsterplace11_aaaxr/theaterpage?date=5/10/2017")


