from pages.base_page import BasePage
from base_element import Elements


class SwapPage(BasePage):
    url = "https://kyberswap.com/#/swap"

    def __init__(self, py):
        super().__init__(py)

    def goto(self):
        BasePage.goto(self, self.url)
        # super.goto(self, self.url)
        return self

    def open_chain(self):
        BasePage.click_x(self, Elements.btn_ethereum)
        return self

    def switch_chain(self, chain):
        # self.py.findx(f"//*[text()='{name}']").first().click()
        BasePage.click_x(self, f"//*[text()='{chain}']")
        return self

    def open_token_list(self):
        BasePage.click(self, Elements.btn_ethereum)

    def click_maximun_return(self):
        pass

    def click_lowest_gas(self):
        pass
