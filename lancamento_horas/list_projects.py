def projetos(args):
    from splinter import Browser
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
        projects = [o for o in browser.find_by_id("novaPanelForm:projeto").first.find_by_css("option")]
        print("PROJECT \tVALUE")
        [print(o.text.strip() + "\t" + o.value.strip()) for o in projects]
