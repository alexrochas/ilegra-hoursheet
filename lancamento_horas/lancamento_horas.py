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
    browser.find_by_name("form:lancarAtividade").click()
    browser.is_element_visible_by_css(".savePanelCDiv")
    # Remove read only from date field
    browser.execute_script("document.getElementsByName('novaPanelForm:dataInputDate')[0].readOnly = false")

    browser.fill("novaPanelForm:dataInputDate", args.date)
    browser.fill("novaPanelForm:strDataHoraInicio", args.start.replace(':', ''))
    browser.fill("novaPanelForm:strDataHoraFim", args.finish.replace(':', ''))
    browser.find_by_id("novaPanelForm:projeto").first.select(args.project)
    time.sleep(2)
    #browser.find_by_id("novaPanelForm:subProjeto").first.select(args.subProject)
    #time.sleep(2)
    browser.find_by_id("novaPanelForm:tipoAtividade").first.select(args.type)
    time.sleep(2)
    browser.fill("novaPanelForm:descricao", args.description)
    if str.lower(input("Everything work until this point.\r\n"
                     + str(args) + "\r\n"
                     + "Push change?[Y/N] ")) == "y":
        browser.find_by_name("novaPanelForm:salvar").click()
        if browser.is_text_present('Atividade lanÃ§ada com sucesso!'):
            print("Done.")
        else:
            print("An unexpected error occur, please try again.")
    else:
        print("Canceled.")
