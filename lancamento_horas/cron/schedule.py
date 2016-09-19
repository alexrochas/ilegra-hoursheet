# -*- coding: utf-8 -*-

# Use this file to easily define all of your cron jobs.
#
# It's helpful to understand cron before proceeding.
# http://en.wikipedia.org/wiki/Cron
#
# Learn more: http://github.com/fengsp/plan

import os
from plan import Plan

cron = Plan()
cron.name = 'Lancamento de horas'
cron.user = 'alex'

path = os.path.dirname(os.path.abspath(__file__))
stdout_config = dict(stdout='/tmp/lancar_horas_out.log', stderr='/tmp/lancar_horas_err.log')
command = "cron.py"
cron.script(command, path=path, every='saturday', output=stdout_config)

if __name__ == "__main__":
    cron.run('update')
