from bs4 import BeautifulSoup
import urllib.request



url = "http://www.fandango.com/regalwebsterplace11_aaaxr/theaterpage"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "html.parser")
soup.prettify()

#print(soup)
#based on the day, list movies, times, and prices

def Soup_time():

    #TITLES
    movie_titles_list = [x.text.strip() for x in soup.findAll("a", {"class": "dark showtimes-movie-title"})]

    #DATES
    dates = [x.text.strip() for x in soup.findAll("a", {"class": "date-area"})]
    dates = [x.replace('\n\n', ', ') for x in dates]
    dates = [x.replace('\n', ' ') for x in dates]
    dates = dates[:7]

    #URLS
    urls = [x.get('href') for x in soup.findAll("a", {"class": "date-area"})]
    urls = urls[:7]

    #TIMES
    times = [x.text.strip() for x in soup.findAll("time", {"class": "timeInfo"})]

    print(movie_titles_list)
    print(times)
    print(dates)
    print(urls)



if __name__ == "__main__":
    Soup_time()

