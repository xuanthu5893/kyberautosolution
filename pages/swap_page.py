from pages.base_page import BasePage


class SwapPage(BasePage):
    url = "https://kyberswap.com/#/swap"

    def __init__(self, py):
        super().__init__(py)

    def goto(self):
        BasePage.goto(self, self.url)
        # super.goto(self, self.url)
        return self

    def open_chain(self):
        # self.py.findx("//*[text()='Ethereum']").first().click()
        BasePage.click_x(self, "//*[text()='Ethereum']")
        return self

    def switch_chain(self, chain="BSC"):
        # self.py.findx(f"//*[text()='{name}']").first().click()
        BasePage.click_x(self, f"//*[text()='{chain}']")
        return self
