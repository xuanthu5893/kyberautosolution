from pages.base_page import BasePage
from utils.route import Route
from elements.base_element import Elements


class PoolPage(BasePage):

    def __init__(self, py):
        super().__init__(py)

    def goto(self):
        BasePage.goto(self, Route.pool_page_url)
        return self

    def open_chain(self):
        BasePage.click(self, Elements.btn_ethereum)
        return self

    def switch_chain(self, chain):
        BasePage.click(self, f"//*[text()='{chain}']")
        return self

    def connect_wallet(self):
        BasePage.click(self, Elements.btn_connect_wallet)

    def get_number_page(self):
        BasePage.text(self, Elements.page_number)

    def create_new_pool(self):
        BasePage.click(self, Elements.btn_create_new_pool)

    def check_displayed(self, text):
        BasePage.is_displayed(self, text)

    def click_information(self):
        BasePage.click(self, self.item_info)
