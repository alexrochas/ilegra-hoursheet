import pprint

from lxml import html
import argparse
import time
from splinter import Browser
from configobj import ConfigObj

config = ConfigObj("perfil.config")

parser = argparse.ArgumentParser(description="Push entry to 'lançamento de horas'")
parser.add_argument('-s', '--start', help='start hour with format hh/mm', default=time.strftime("%H%M"))
parser.add_argument('-f', '--finish', help='finish hour with format hh/mm', default=time.strftime("%H%M"))
parser.add_argument('-d', '--date', help='reference date', default=time.strftime("%d/%m/%Y"))
parser.add_argument('-u', '--user', help='user name', default=config.get("usuario"))
parser.add_argument('-p', '--password', help='password', default=config.get("senha"))
parser.add_argument('-D', '--description', help='task description', default="")
parser.add_argument('-P', '--project', help='project id', default=config.get("projeto"))
parser.add_argument('-S', '--subProject', help='sub-project id', default=config.get("subProjeto"))
parser.add_argument('-T', '--type', help='activity type id', default=config.get("tipoAtividade"))
args = parser.parse_args()

with Browser("phantomjs") as browser:
    # Visit URL
    url = "http://sistemas2.ilegra.com/lancamentohoras/login.faces"
    browser.visit(url)
    browser.fill('form:usuario', args.user)
    browser.fill('form:senha', args.password)
    # Find and click the 'search' button
    button = browser.find_by_name("form:acessarSistema")
    # Interact with elements
    button.click()
    url = "http://sistemas2.ilegra.com/lancamentohoras/lancamento_horas.faces"
    # Workaround, you gonna need it
    browser.visit(url)
    page_content = browser.driver.page_source
    tree = html.fromstring(page_content)

    datas = tree.xpath("//span[re:test(@id, 'formDataTable:table:\d+:data$')]/text()",
                     namespaces={'re': "http://exslt.org/regular-expressions"})
    horas_inicio = tree.xpath("//span[re:test(@id, 'formDataTable:table:\d+:dataHoraInicio$')]/text()",
                     namespaces={'re': "http://exslt.org/regular-expressions"})
    horas_fim = tree.xpath("//span[re:test(@id, 'formDataTable:table:\d+:dataHoraFim$')]/text()",
                     namespaces={'re': "http://exslt.org/regular-expressions"})
    projetos = tree.xpath("//span[re:test(@id, 'formDataTable:table:\d+:projeto$')]/text()",
                     namespaces={'re': "http://exslt.org/regular-expressions"})
    horas = tree.xpath("//span[re:test(@id, 'formDataTable:table:\d+:horas$')]/text()",
                     namespaces={'re': "http://exslt.org/regular-expressions"})

    linhas = zip(datas, horas_inicio, horas_fim, horas, projetos)

    resultado = {}
    for data, hora_inicio, hora_fim, total, projeto in linhas:
        if resultado.get(data):
            resultado[data] = float(resultado[data]) + float(total)
        else:
            resultado[data] = float(total)

    total = 0
    for data in resultado:
        total = total + resultado[data]

    for data in resultado:
        import datetime
        resultado[data] = str(datetime.timedelta(seconds=(resultado[data] * 3600)))

    pprint.pprint(resultado)
    print("TOTAL = " + str(datetime.timedelta(seconds=(total * 3600)).total_seconds() / 3600))

