import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from lancamento_horas import lancar_horas, list_projects, list_subprojects, list_activity_type, dimed
from configobj import ConfigObj
import argparse
import time

config = ConfigObj("../conf/perfil.config")

commands = {
    'lancar': lancar_horas.lancar,
    'projetos': list_projects.projetos,
    'sub-projetos': list_subprojects.sub_projetos,
    'atividades': list_activity_type.atividades,
    'dimed': dimed.total_horas
}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Cliente para lançamento de horas")
    subparser = parser.add_subparsers(help="Lança horas no sistema | Lista projetos, sub-projetos e atividades",
                                      dest="command")
    # lancar
    lancar_parser = subparser.add_parser('lancar')
    lancar_parser.add_argument('-s', '--start', help='start hour with format hh/mm', default=time.strftime("%H%M"))
    lancar_parser.add_argument('-f', '--finish', help='finish hour with format hh/mm', default=time.strftime("%H%M"))
    lancar_parser.add_argument('-d', '--date', help='reference date', default=time.strftime("%d/%m/%Y"))
    lancar_parser.add_argument('-u', '--user', help='user name', default=config.get("usuario"))
    lancar_parser.add_argument('-p', '--password', help='password', default=config.get("senha"))
    lancar_parser.add_argument('-D', '--description', help='task description', default="")
    lancar_parser.add_argument('-P', '--project', help='project id', default=config.get("projeto"))
    lancar_parser.add_argument('-S', '--subProject', help='sub-project id', default=config.get("subProjeto"))
    lancar_parser.add_argument('-T', '--type', help='activity type id', default=config.get("tipoAtividade"))

    # listar projeto
    projeto_parser = subparser.add_parser('projetos')
    projeto_parser.add_argument('-u', '--user', help='user name', default=config.get("usuario"))
    projeto_parser.add_argument('-p', '--password', help='password', default=config.get("senha"))

    # total de horas para dimed
    projeto_parser = subparser.add_parser('dimed')
    projeto_parser.add_argument('-u', '--user', help='user name', default=config.get("usuario"))
    projeto_parser.add_argument('-p', '--password', help='password', default=config.get("senha"))

    # listar sub-projeto
    sub_projeto_parser = subparser.add_parser('sub-projetos')
    sub_projeto_parser.add_argument('-u', '--user', help='user name', default=config.get("usuario"))
    sub_projeto_parser.add_argument('-p', '--password', help='password', default=config.get("senha"))
    sub_projeto_parser.add_argument('-P', '--project', help='project id', default=config.get("projeto"))

    # listar atividades_projeto
    atividade_parser = subparser.add_parser('atividades')
    atividade_parser.add_argument('-u', '--user', help='user name', default=config.get("usuario"))
    atividade_parser.add_argument('-p', '--password', help='password', default=config.get("senha"))
    atividade_parser.add_argument('-P', '--project', help='project id', default=config.get("projeto"))

    args, unkown = parser.parse_known_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    commands[args.command](args)
