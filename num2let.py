# -* codding : utf-8
# supported python version: 3.6

__author__ = "Djoudi Benarfa"
__create_date__ = "12/03/2017"
__version__ = "0.1"
__email__ = "dbenarfa@outlook.com"



def split_number(number):
    """
    Splits the given number in to thousand grouped list
    ex: 12,345,678 => ['12','345','678']
    :param number: the number to be splitted
    :return: a list of splitted number (thousand grouped numbers)
    NOTE: The numbers in the list are converted into strings
    """

    if '.' in str(number):
        list_number = f"{number}".split('.')
        fpart = int(list_number[0])
        lpart = int(list_number[1])
        first_part = f"{fpart:_}".split('_')
        last_part = f"{lpart:_}".split('_')
        return first_part, last_part
    else:
        first_part = list(map(int, f"{number:_}".split('_')))
        return first_part