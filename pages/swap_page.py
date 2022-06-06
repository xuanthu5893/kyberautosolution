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
        pass

    def click_lowest_gas(self):
        pass

    def open_setting_dialog(self):
        BasePage.click(self, SwapPageElements.btn_advance_setting)

    def get_title(self):
        return BasePage.get_text(self, SwapPageElements.title_advance_setting)

    def input_slippage(self, slippage_value):
        BasePage.input(self, SwapPageElements.slippage_text_field, slippage_value)

    def check_displayed(self, text):
        return BasePage.is_displayed(self, text)

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
                                                                                       "-1 kYQzoT "
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
