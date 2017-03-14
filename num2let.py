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


def convert_number(number):
    sign = 'moins ' if str(number)[0] == '-' else ''

    if number == '000':
        return ""

    got_zero = ''
    # if len(number) > 1:
    #     for n in number:
    #         if n == '0':
    #             got_zero += "zero "
    #         else:
    #             break
    # print(got_zero)

    number = str(abs(int(number)))
    if int(number) <= 16:
        return f"{sign}{got_zero}{numbers_less_17[number]}"
    elif int(number) > 99:
        hundreds = numbers_less_17[int(str(number)[0])] if int(str(number)[0]) > 1 else ""
        if int(str(number)[1:]) > 0:
            return f"{sign}{got_zero}{hundreds} {cent_label} {convert_number(str(number)[1:])}"
        else:
            return f"{sign}{got_zero}{hundreds} {cent_label}"
    else:
        # Prennent un trait d'union tous les nombres composés inférieurs à 100 ne se terminant pas en 1 sauf 81 et 91
        if number[0] in ('8', '9') or number[1] != '1':
            separator = "-"
        elif number[1] == '1':
            separator = f" {et_label} "
        else:
            separator = ' '
        if number[0] in ("7", "9") and number[1] != 0:
            return f"{sign}{got_zero}{dix[int(number[0])-1]}{separator}" \
                   f"{convert_number(str(int(number[1])+10))}"

        if int(number[1]) == 0:
            return f"{sign}{got_zero}{dix[int(number[0])]}"
        else:
            return f"{sign}{got_zero}{dix[int(number[0])]}{separator}" \
                   f"{numbers_less_17[int(number[1])]}"

def dispatch(numbers_list):
    global billiard_label, billion_label, milliard_label, million_label, mille_label

    if len(numbers_list) == 6:
        # Billion
        return f"{convert_number(numbers_list[0])} {billiard_label} {dispatch(numbers_list[1:])}"
    elif len(numbers_list) == 5:
        # Billion
        if float(numbers_list[0]) == 0:
            billion_label = ""
        return f"{convert_number(numbers_list[0])} {billion_label} {dispatch(numbers_list[1:])}"
    elif len(numbers_list) == 4:
        # Milliard
        if float(numbers_list[0]) == 0:
            milliard_label = ""
        return f"{convert_number(numbers_list[0])} {milliard_label} {dispatch(numbers_list[1:])}"
    elif len(numbers_list) == 3:
        # Million
        if float(numbers_list[0]) == 0:
            million_label = ""
        return f"{convert_number(numbers_list[0])} {million_label} {dispatch(numbers_list[1:])}"
    elif len(numbers_list) == 2:
    # Mille
        if float(numbers_list[0]) == 0:
            mille_label = ""
        thousand = convert_number(numbers_list[0]) if float(numbers_list[0]) > 1 else ""
        return f"{thousand}{mille_label+' ' if mille_label !='' else ''}{dispatch(numbers_list[1:])}"
    elif len(numbers_list) == 1:
        # Cent
        return f"{convert_number(numbers_list[0])}"
    else:
        return far_number


def convert(number, currency='', unit='centime'):
    number_parts = split_number(number)

    if isinstance(number_parts, tuple):
        return f"{dispatch(number_parts[0])}{' '+vergule_label+' ' if currency == '' else ' '+currency+' '+et_label+' '}" \
               f"{dispatch(number_parts[1])} {'' if currency == '' else unit}".strip()
    else:
        return f"{dispatch(number_parts)}{' '+currency if currency != '' else ''}".strip()

if __name__ == '__main__':
    print(convert(1223.23, "euro", "centime d'euro"))