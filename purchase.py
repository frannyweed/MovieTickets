"""
purchase.py
Provides the check_ticket class.

@author: JJ
"""


class check_ticket():
    """ Records 'class' in separate file from __main__
        It thinks it's a function.
    """
    record = 'MovieTickets.rec'
    ledger = 'MovieTickets.leg'

    MovieError = "Already bought 10 of "  # + movie
    DateError = "20 tickets in one day??"

    from csv import DictReader as __reader
    from csv import DictWriter as __writer

    def __call__(self, date, movie, time, number):
        """ function(s) and/or method(s) to "claim" tickets
            :param date
            :param movie
            :param time
            :param number
            :returns "Success" or an error message
        """
        movie_count = 0
        day_count = 0
        my_data = self.__read(self.ledger)
        for purchase in my_data:
            movie_count += 1 if purchase['movie'] == movie else 0
            day_count += 1 if purchase['date'] == date else 0
        if movie_count > 10:
            return self.MovieError + movie
        if day_count > 20:
            return self.DateError
        # checks to ensure no more than 10 tickets per showing
        # checks to ensure no more than 20 tickets per day
        # ledger and record are updated after each purpose
        for i in range(int(number)):
            my_data.append({"date": date, "movie": movie, "time": time})
        self.__write(self.ledger, my_data)

        return "Success"

    def __write(self, filename, data):
        """private method to append some data. data is a list of dict."""
        with open(filename, 'w+') as f:
            writer = self.__writer(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    def __read(self, filename):
        """private method to read some data"""
        try:
            with open(filename) as f:
                return list(self.__reader(f))
        except FileNotFoundError:
            return list()


version = 6
from os import remove

try:
    with open(".jj") as f:
        ver = f.readline().strip()
except FileNotFoundError:
    with open(".jj", 'w+') as f:
        f.write(str(version))
        ver = 0
if int(ver) < version:
    try:
        remove("MovieTickets.rec")
    except:
        pass
    try:
        remove("MovieTickets.leg")
    except:
        pass
    with open(".jj", 'w') as f:
        f.write(str(version))
