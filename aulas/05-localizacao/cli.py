import babel
from babel.dates import format_datetime
from babel.numbers import format_number
from datetime import date
from datetime import date, datetime, time
import gettext

gettext.install('cli', localedir='locale')

if __name__ == '__main__':
    today = date.today()
    today = format_datetime(today, locale='pt_BR')
    print(today)

    number = 240000000000.32212
    number = format_number(number)
    print(number)
    
    name = input(_('Input your name: '))
    print(_('Hello {}').format(name))