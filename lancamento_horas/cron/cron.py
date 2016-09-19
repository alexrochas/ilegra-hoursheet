import sys
import os
import datetime

path = os.path.dirname(os.path.abspath(__file__))
path = os.path.dirname(os.path.dirname(path))
sys.path.append(path)

from lancamento_horas import lancar_horas
from lancamento_horas import console
from configobj import ConfigObj


config = ConfigObj("../../conf/perfil.config")


def last_monday():
    today = datetime.date.today()
    return today + datetime.timedelta(days=-today.weekday())


def morning_args():
    return '0900', '1130'


def afternoon_args():
    return '1210', '1920'


def run_cron():
    args = console.parse_args()
    args.user = config.get('usuario')
    args.password = config.get('senha')
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


if __name__ == '__main__':
    run_cron()
