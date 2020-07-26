def blue(phrase=''):
    if phrase == '':
        return '\033[34m'
    else:
        return f'\033[34m{phrase}\033[m'


def green(phrase=''):
    if phrase == '':
        return '\033[32m'
    else:
        return f'\033[32m{phrase}\033[m'


def purple(phrase=''):
    if phrase == '':
        return '\033[35m'
    else:
        return f'\033[35m{phrase}\033[m'


def white(phrase=''):
    if phrase == '':
        return '\033[30m'
    else:
        return f'\033[30m{phrase}\033[m'


def red(phrase=''):
    if phrase == '':
        return '\033[31m'
    else:
        return f'\033[31m{phrase}\033[m'


def yellow(phrase=''):
    if phrase == '':
        return '\033[33m'
    else:
        return f'\033[33m{phrase}\033[m'


def whiteblue(phrase=''):
    if phrase == '':
        return '\033[36m'
    else:
        return f'\033[36m{phrase}\033[m'


def grey(phrase=''):
    if phrase == '':
        return '\033[37m'
    else:
        return f'\033[37m{phrase}\033[m'


def erase(phrase=''):
    if phrase == '':
        return '\033[m'
    else:
        return f'\033[m{phrase}\033[m'


def bolder(phrase=''):
    if phrase == '':
        return '\033[1m'
    else:
        return f'\033[1m{phrase}\033[m'
