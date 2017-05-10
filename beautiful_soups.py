from bs4 import BeautifulSoup
import urllib.request





#print(soup)
#based on the day, list movies, times, and prices

def get_dates():
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
    for i in urls:
        print(i)

    #print(dates)
    #print(urls)

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
    times = [x.text.strip() for x in soup.findAll("time", {"class": "timeInfo"})]
    print(times)

if __name__ == "__main__":
    get_dates()
    get_movies("http://www.fandango.com/regalwebsterplace11_aaaxr/theaterpage?date=5/10/2017")
    get_times("http://www.fandango.com/regalwebsterplace11_aaaxr/theaterpage?date=5/10/2017")



