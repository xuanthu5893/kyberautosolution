class TestSwapPage:
    def test_switch_chain(py, kyber):
        kyber.swap.goto().open_chain().switch_chain()
        assert True
