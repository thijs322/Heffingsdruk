import datetime
import time

def get_next_ten_numbers(number):
    """
    Just gets the next ten numbers of a given number
    :param number: random integer
    """
    return list(range(number + 1, number + 10))
