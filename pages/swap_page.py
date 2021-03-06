import time

from pages.base_page import BasePage
from elements.base_element import Elements
from elements.swap_page_elements import SwapPageElements
from utils.route import Route


class SwapPage(BasePage):

    def __init__(self, py):
        super().__init__(py)

    def goto(self):
        BasePage.goto(self, Route.swap_page_url)
        # super.goto(self, self.url)
        return self

    def open_chain(self):
        BasePage.click(self, SwapPageElements.open_chains)
        return self

    def switch_chain(self, chain):
        # self.py.findx(f"//*[text()='{name}']").first().click()
        BasePage.click(self, f"//*[text()='{chain}']")
        return self

    def open_token_list(self):
        BasePage.click(self, SwapPageElements.btn_ethereum)

    def click_maximum_return(self):
        BasePage.click(self, SwapPageElements.btn_maximum_return)

    def click_lowest_gas(self):
        BasePage.click(self, SwapPageElements.btn_lowest_gas)

    def open_setting_dialog(self):
        BasePage.click(self, SwapPageElements.btn_advance_setting)

    def get_title(self):
        return BasePage.get_text(self, SwapPageElements.title_advance_setting)

    def input_slippage(self, slippage_value):
        BasePage.input(self, SwapPageElements.slippage_text_field, slippage_value)

    def check_displayed(self, text):
        return BasePage.is_displayed(self, "//*[text()='" + text + "']")

    def get_minimum_received_value(self):
        return BasePage.get_text(self, SwapPageElements.minimum_received_value)

    def open_more_information(self):
        BasePage.click(self, SwapPageElements.btn_more_information)

    def get_gas_fee_value(self):
        return BasePage.get_text(self, SwapPageElements.gas_fee_value)

    def get_price_impact_value(self):
        return BasePage.get_text(self, SwapPageElements.price_impact_value)

    def input_amount_in(self, amount):
        BasePage.clear_text(self, SwapPageElements.amount_in)
        BasePage.input(self, SwapPageElements.amount_in, amount)

    def get_amount_out(self):
        time.sleep(3)
        return BasePage.get_property(self, SwapPageElements.amount_out, "value")

    def get_currency_input_value(self):
        return BasePage.get_text(self, SwapPageElements.currency_input)

    def get_currency_output_value(self):
        return BasePage.get_text(self, SwapPageElements.current_output)

    def get_slippage_value(self):
        return BasePage.get_text(self, SwapPageElements.slippage_value)

    def get_trx_time_limit(self):
        return BasePage.get_property(self, SwapPageElements.transaction_time_limit_field, "placeholder")

    def input_trx_time_limit_value(self, value):
        BasePage.input(self, SwapPageElements.transaction_time_limit_field, value)

    def get_advance_mode(self):
        if (BasePage.get_attribute(self, SwapPageElements.advance_mode_on, "class") == "Toggle__ToggleElement-k4pnr9"
                                                                                       "-1 kYQzoT"
                and BasePage.get_attribute(self, SwapPageElements.advance_mode_off,
                                           "class") == "Toggle__ToggleElement-k4pnr9-1 jseynB"):
            return False
        return True

    def click_on_off_advance_mode(self):
        BasePage.click(self, SwapPageElements.btn_advance_config)

    def get_advance_mode_term(self):
        return BasePage.get_text(self, SwapPageElements.advance_mode_term)

    def get_advance_mode_term_1(self):
        return BasePage.get_text(self, SwapPageElements.advance_mode_term_1)

    def select_cancel_advance_mode(self):
        BasePage.click(self, SwapPageElements.btn_cancel)

    def select_confirm_advance_mode(self):
        BasePage.click(self, SwapPageElements.btn_confirm)

    def input_advance_mode_text_field(self, text):
        BasePage.input(self, SwapPageElements.advance_mode_confirm_text_field, text)

    def get_max_slippage_warning_mgs(self):
        return BasePage.get_text(self, SwapPageElements.max_slippage_waring_mgs)

    def switch_basic_view_chart(self):
        BasePage.click(self, SwapPageElements.btn_basic_view_chart)
        time.sleep(10)

    def switch_pro_view_chart(self):
        BasePage.click(self, SwapPageElements.btn_pro_view_chart)
        time.sleep(10)

    def get_currency_input_info(self):
        BasePage.click(self, SwapPageElements.btn_info)
        BasePage.click(self, SwapPageElements.btn_currency_input_infor)
        time.sleep(3)
        print("\n" + BasePage.get_text(self, SwapPageElements.btn_currency_input_infor))
        for x in range(1, 10):
            currency_label_name = SwapPageElements.currency_label_name + "[" + str(x) + "]"
            currency_label_value = SwapPageElements.currency_label_value + "[" + str(x) + "]"
            print(
                BasePage.get_text(self, currency_label_name) + "------" + BasePage.get_text(self, currency_label_value))

    def get_currency_output_info(self):
        BasePage.click(self, SwapPageElements.btn_info)
        BasePage.click(self, SwapPageElements.btn_currency_output_infor)
        time.sleep(3)
        print("\n" + BasePage.get_text(self, SwapPageElements.btn_currency_output_infor))
        for x in range(1, 10):
            currency_label_name = SwapPageElements.currency_label_name + "[" + str(x) + "]"
            currency_label_value = SwapPageElements.currency_label_value + "[" + str(x) + "]"
            print(
                BasePage.get_text(self, currency_label_name) + "------" + BasePage.get_text(self, currency_label_value))

    def select_currency_input(self):
        BasePage.click(self, SwapPageElements.currency_input)

    def get_list_common_base_token(self):
        list_locator = BasePage.find_elements(self, SwapPageElements.list_common_base_token)
        list_token = []
        for x in list_locator:
            token = x.text()
            list_token.append(token)
        return list_token

    def search_token(self, token_name):
        BasePage.input(self, SwapPageElements.search_text_field, token_name)

    def get_token_search_result(self):
        list_locator = BasePage.find_elements(self, SwapPageElements.search_result)
        list_token = []
        for x in list_locator:
            token = x.text()
            list_token.append(token)
        return list_token


