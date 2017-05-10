"""
purchase.py
Provides the Records class.

- 
- both record and ledger kept as csv files 
- checks to ensure no more than 10 tickets per showing
- checks to ensure no more than 20 tickets per day
- ledger and record are updated after each purpose

"""


class Records():
    """Records class in separate file from __main__"""
    record = 'MovieTickets.rec'
    ledger = 'MovieTickets.leg'
    from csv import DictReader as __reader
    from csv import DictWriter as __writer

    def __init__(self):
        pass

    def claim_tickets(self, date, movie, time, number):
        """function(s) and/or method(s) to "claim" tickets
        :param date
        :param movie
        :param time
        :param number
        """

    def __write(self, filename, data):
        """private method to write some data. data is a list of dict."""
        with open(filename, 'w') as f:
            writer = self.__writer(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    def __read(self, filename):
        """private method to read some data"""
        with open(filename) as f:
            return [dict(row) for row in self.__reader(f)]