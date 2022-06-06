def test_pair_value(kyber):
    # Open swap page
    kyber.swap.goto().open_chain().switch_chain("BNB Chain")
    # Check default value of input currency is ETH
    assert (kyber.swap.get_currency_input_value()) == "BNB"
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

