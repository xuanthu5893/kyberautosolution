def test_verify_page(kyber):
    kyber.pool.goto().open_chain().switch_chain("BSC")
    assert kyber.pool.get_number_page() == "Page 1 of 16"


def test_create_new_pool_page(kyber):
    kyber.pool.goto().open_chain().switch_chain("BSC")
    kyber.pool.create_new_pool().click_information()
    assert kyber.pool.check_displayed("//div[contains(text(),'Add Liquidity')]") == True
