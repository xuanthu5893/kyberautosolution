import time

from elements.analytics_page_elements import AnalyticsPageElements
from pages.base_page import BasePage
from utils.route import Route


class AnalyticsPage(BasePage):

    def __init__(self, py):
        super().__init__(py)

    def goto(self):
        BasePage.goto(self, Route.analyst_page_url)
        return self

    def get_trading_volume(self):
        return BasePage.get_text(self, AnalyticsPageElements.trading_volume_value)

    def change_trading_volume_all_time(self):
        BasePage.click(self, AnalyticsPageElements.btn_trading_volume_all_time)

    def change_trading_volume_24h(self):
        BasePage.click(self, AnalyticsPageElements.btn_trading_volume_24h)

    def get_fee_24h_value(self):
        return BasePage.get_text(self, AnalyticsPageElements.fee_24h_value)

    def get_transaction_24h_value(self):
        return BasePage.get_text(self, AnalyticsPageElements.transaction_24h_value)

    def get_list_top_token(self):
        time.sleep(10)
        list_token_element = BasePage.find_elements(self, AnalyticsPageElements.top_token_info)
        list_token_info = []
        for x in list_token_element:
            token_info = x.text().split("\n")
            list_token_info.append(token_info)
        return list_token_info

    def get_list_top_pairs(self):
        time.sleep(10)
        list_pairs_element = BasePage.find_elements(self, AnalyticsPageElements.top_pairs_info)
        list_pairs_info = []
        for x in list_pairs_element:
            token_info = x.text().split("\n")
            list_pairs_info.append(token_info)
        return list_pairs_info

    def click_swap_btn(self):
        BasePage.click(self, AnalyticsPageElements.btn_swap_menu)
        BasePage.switch_tab(self)
