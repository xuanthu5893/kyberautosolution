import time


def test_pair_value(kyber):
    # Open swap page
    kyber.analytics.goto()
    print(kyber.analytics.get_trading_volume())
    kyber.analytics.change_trading_volume_24h()
    print(kyber.analytics.get_trading_volume())
    print(kyber.analytics.get_fee_24h_value())
    print(kyber.analytics.get_transaction_24h_value())


def test_top_token_data(kyber):
    kyber.analytics.goto()
    list_token = kyber.analytics.get_list_top_token()
    for x in list_token:
        print(x)


def test_top_token_length(kyber):
    kyber.analytics.goto()
    list_token = kyber.analytics.get_list_top_token()
    assert len(list_token) == 5


def test_top_pairs_data(kyber):
    kyber.analytics.goto()
    list_pair = kyber.analytics.get_list_top_pairs()
    for x in list_pair:
        print(x)


def test_top_pairs_length(kyber):
    kyber.analytics.goto()
    list_pair = kyber.analytics.get_list_top_pairs()
    assert len(list_pair) == 5


def test_open_swap_page_by_click_button_in_menu(kyber):
    kyber.analytics.goto()
    kyber.analytics.click_swap_btn()
    time.sleep(20)
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
