from pages.header_nav import HeaderNav


class BasePage:
    def __init__(self, py):
        self.py = py
        self.header = HeaderNav(py)

    def goto(self, url):
        self.py.maximize_window().visit(url)

    def click(self, selector_string):
        self.find_element(selector_string).click()
        # self.py.getx("selector_string").click()

    def text(self, xpath):
        return self.find_element(xpath).text()

    def find_element(self, locator):
        if "//" in locator:
            return self.py.getx(locator)
        else:
            return self.py.get(locator)

    def is_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    def get_web_cookies(self):
        cookies = self.py.get_cookies()
        for x in range(len(cookies)):
            print(cookies[x])
        return cookies

    def get_text(self, locator):
        return self.find_element(locator).text()

    def input(self, selector_string, input_value):
        self.find_element(selector_string).type(input_value)

    def clear_text(self, locator):
        self.find_element(locator).clear()

    def get_property(self, locator, property_name):
        return self.find_element(locator).get_property(property_name)

    def get_attribute(self, locator, attribute_name):
        return self.find_element(locator).get_attribute(attribute_name)

    def find_element_1(self, locator):
        if "//" in locator:
            return self.py.findx(locator)
        else:
            return self.py.find(locator)
