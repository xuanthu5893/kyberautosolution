from pages.header_nav import HeaderNav


class BasePage:
    def __init__(self, py):
        self.py = py
        self.header = HeaderNav(py)

    def goto(self, url):
        self.py.maximize_window().visit(url)

    def click(self, selector_string):
        self.find(selector_string).click()

    def text(self, xpath):
        return self.py.findx(xpath).first().text()

    def find(self, selector_string):
        if selector_string.find("//"):
            return self.py.findx(selector_string).first()
        else:
            return self.py.find(selector_string).first()
