import re
from re import error



def fact(n1):
    f = 1
    for c in range(1, n1+1):
        f *= c
    return f


def triple(n1):
    return n1 * 3


def double(num, form=False):
    result = num*2
    if form:
        result = f'R${result}'
    return result


def half(num, form=False):
    result = num/2
    if form:
        result = f'R${result}'
    return result


def increase(num, percent, form=False):
    percent *= num
    percent /= 100
    result = num + percent
    if form:
        result = f'R${result}'
    return result


def reduce(num, percent, form=False):
    percent *= num
    percent /= 100
    result = num - percent
    if form:
        result = f'R${result:2f}'
    return result


def coin(value):
    value = f'R${value}'
    return value.replace('.', ',')



def readMoney(inputPhrase="", monetaryValue=""):
    """
        It converts monetary values(like U$"45,6", instead of 45.6) for float values that the Python will can read (float)
        To use, bring your input sentence (inputPhrase="your sentece") or a monetary to convert (monetaryValue="54,50", for example)
        ATTENTION: PUT ONLY THE NUMERICAL PART AS PARAMETER
    """
    try:
        if inputPhrase != "":
            val = False
            
            while not val:
                phrase = str(input(f'\033[1;30m{inputPhrase}')).replace(',', '.').strip()
                
                if re.match("^\d+\.\d+$", phrase):
                    val = True
                    return float(phrase)

        if monetaryValue != "":
            val = monetaryValue.replace(',', '.').strip()
            
            if re.match('^\d+\.\d+$', val):
                return float(val)
            else:
                return "An error has ocurred, please verify your values :("
    except:
        return f"An error has ocurred, please verify your values :("        
