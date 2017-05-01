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
    def __init__(self):
        pass

    def write_to_ledger(self,date,movie,time,tickets):
        """a ledger to permanently record each purchase (date,movie,time,tickets)"""
        pass

    def write_to_record(self):
        """a record to permanently record total purchase for each day and showing"""

    def claim_tickets(self):
        """function(s) and/or method(s) to "claim" tickets"""
