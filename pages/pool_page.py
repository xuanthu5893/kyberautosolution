from pages.base_page import BasePage


class PoolPage(BasePage):
    url = "https://kyberswap.com/#/pools"

    def __init__(self, py):
        super().__init__(py)

    def goto(self):
        BasePage.goto(self, self.url)
        return self
