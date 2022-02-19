from xml.dom.minidom import Element
from pages.header_nav import HeaderNav


class BasePage:
    def __init__(self, py):
        self.py = py
        self.header = HeaderNav(py)

    def goto(self, url):
        self.py.maximize_window().visit(url)

    def click_x(self, xpath):
        return self.py.findx(xpath).first().click()

    def text(self, xpath):
        return self.py.findx(xpath).first().text()
