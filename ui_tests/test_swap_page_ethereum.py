from utils.resources import Resources


def test_pair_value(kyber):
    # Open swap page
    kyber.swap.goto()
    # Check default value of input currency is ETH
    assert (kyber.swap.get_currency_input_value()) == "ETH"
    # Check default value of output currency is KNC
    assert (kyber.swap.get_currency_output_value()) == "KNC"
    # Change value of amount in
    kyber.swap.input_amount_in("12")
    # Get value of amount out
    print(kyber.swap.get_amount_out())
    # Open more information
    kyber.swap.open_more_information()
    print(kyber.swap.get_minimum_received_value())
    print(kyber.swap.get_gas_fee_value())
    print(kyber.swap.get_price_impact_value())


def test_input_invalid_value_for_max_slippage(kyber):  # Input invalid value of Max Slippage
    kyber.swap.goto()
    kyber.swap.open_setting_dialog()
    assert (kyber.swap.get_title()) == Resources.advance_setting_title
    kyber.swap.input_slippage("60")
    assert (kyber.swap.get_max_slippage_warning_mgs()) == Resources.max_slippage_warning_mgs_2


def test_input_valid_value_for_max_slippage_1(kyber):
    # Open swap page
    kyber.swap.goto()
    kyber.swap.open_setting_dialog()
    assert (kyber.swap.get_title()) == Resources.advance_setting_title
    kyber.swap.input_slippage("12")
    assert (kyber.swap.get_max_slippage_warning_mgs()) == Resources.max_slippage_warning_mgs_1
    kyber.swap.open_setting_dialog()
    assert (kyber.swap.get_slippage_value()) == "Max Slippage: 12%"


def test_input_valid_value_for_max_slippage_2(kyber):
    # Open swap page
    kyber.swap.goto()
    kyber.swap.open_setting_dialog()
    assert (kyber.swap.get_title()) == Resources.advance_setting_title
    kyber.swap.input_slippage("5")
    assert (kyber.swap.get_max_slippage_warning_mgs()) != Resources.max_slippage_warning_mgs_1
    assert (kyber.swap.get_max_slippage_warning_mgs()) != Resources.max_slippage_warning_mgs_2
    kyber.swap.open_setting_dialog()


def test_input_valid_value_for_max_slippage_3(kyber):
    kyber.swap.goto()
    kyber.swap.open_setting_dialog()
    assert (kyber.swap.get_title()) == Resources.advance_setting_title
    kyber.swap.input_slippage("0.1")
    assert (kyber.swap.check_displayed("//div[contains(text(),'Your transaction may fail')]")) == True
    kyber.swap.open_setting_dialog()
    assert (kyber.swap.get_slippage_value()) == "Max Slippage: 0.1%"


def test_default_trx_time_limit(kyber):
    kyber.swap.goto()
    kyber.swap.open_setting_dialog()
    assert (kyber.swap.get_trx_time_limit()) == "20"


def test_change_valid_value_trx_time_limit(kyber):
    kyber.swap.goto()
    kyber.swap.open_setting_dialog()
    kyber.swap.input_trx_time_limit_value("15")
    kyber.swap.open_setting_dialog()
    kyber.swap.open_setting_dialog()
    assert (kyber.swap.get_trx_time_limit()) == "15"


def test_change_invalid_value_trx_time_limit(kyber):
    kyber.swap.goto()
    kyber.swap.open_setting_dialog()
    kyber.swap.input_trx_time_limit_value("15")
    kyber.swap.open_setting_dialog()
    kyber.swap.open_setting_dialog()
    assert (kyber.swap.get_trx_time_limit()) == "15"
    kyber.swap.input_trx_time_limit_value("ABCDE")
    kyber.swap.open_setting_dialog()
    kyber.swap.open_setting_dialog()
    assert (kyber.swap.get_trx_time_limit()) == "15"


def test_change_advance_mode(kyber):
    kyber.swap.goto()
    kyber.swap.open_setting_dialog()
    assert (kyber.swap.get_advance_mode()) == False
    kyber.swap.click_on_off_advance_mode()
    assert (kyber.swap.get_advance_mode_term()) == Resources.advance_mode_term_1
    assert (kyber.swap.get_advance_mode_term_1()) == Resources.advance_mode_term_2


def test_change_advance_mode_select_cancel(kyber):
    kyber.swap.goto()
    kyber.swap.open_setting_dialog()
    assert (kyber.swap.get_advance_mode()) == False
    kyber.swap.click_on_off_advance_mode()
    kyber.swap.select_cancel_advance_mode()
    kyber.swap.open_setting_dialog()
    assert (kyber.swap.get_advance_mode()) == False


def test_change_advance_mode_select_invalid_value(kyber):
    kyber.swap.goto()
    kyber.swap.open_setting_dialog()
    assert (kyber.swap.get_advance_mode()) == False
    kyber.swap.click_on_off_advance_mode()
    kyber.swap.input_advance_mode_text_field("Test")
    kyber.swap.select_confirm_advance_mode()


def test_change_advance_mode_select_valid_value(kyber):
    kyber.swap.goto()
    kyber.swap.open_setting_dialog()
    assert (kyber.swap.get_advance_mode()) == False
    kyber.swap.click_on_off_advance_mode()
    kyber.swap.input_advance_mode_text_field("confirm")
    kyber.swap.select_confirm_advance_mode()
    kyber.swap.open_setting_dialog()
    assert (kyber.swap.get_advance_mode()) == True
