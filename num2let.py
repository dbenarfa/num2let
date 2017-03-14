# -* codding : utf-8
# supported python version: 3.6

__author__ = "Djoudi Benarfa"
__create_date__ = "12/03/2017"
__version__ = "0.1"
__email__ = "dbenarfa@outlook.com"

numbers_less_17 = {1: "un",
                       2: "deux",
                       3: "trois",
                       4: "quatre",
                       5: "cinq",
                       6: "six",
                       7: "sept",
                       8: "huit",
                       9: "neuf",
                       0: "zero",
                       10: "dix",
                       11: "onze",
                       12: "douze",
                       13: "treize",
                       14: "quatorze",
                       15: "quinze",
                       16: "seize"
                       }
dix = {1: "dix",
       2: "vingt",
       3: "trente",
       4: "quarante",
       5: "cinquante",
       6: "soixante",
       7: "soixante-dix",
       8: "quatre-vingt",
       9: "quatre-vingt-dix"
       }

cent_label = "cent"
mille_label = "mille"
million_label = "million"
milliard_label = "milliard"
billion_label = "billion"
billiard_label = "billiard"
far_number = "ou allez vous.."
plus = "s"
vergule_label = "vergule"
et_label = "et"


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