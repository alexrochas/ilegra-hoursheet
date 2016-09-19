import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
path = os.path.dirname(os.path.dirname(path))
sys.path.append(path) #the directory that contains my_pkg

from lancamento_horas import lancar_horas
from lancamento_horas import console
import datetime


def last_monday():
    today = datetime.date.today()
    return today + datetime.timedelta(days=-today.weekday())


def morning_args():
    return '0900', '1130'


def afternoon_args():
    return '1210', '1920'

args = console.parse_args()
args.user = 'alex.silva'
args.password = 'ilegra0712'
args.yes = 'y'
args.start, args.finish = morning_args()
args.project = 1981
args.subProject = 'SELECIONE...'
args.type = 20
args.description = '[place holder]'
args.date = last_monday().strftime('%d/%m/%Y')

lancar_horas.lancar(args)

args.start, args.finish = afternoon_args()

lancar_horas.lancar(args)
