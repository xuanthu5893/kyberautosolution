from pages.swap_page import SwapPage


class KyberPages:
    def __init__(self, py):
        self.py = py
        self.swap = SwapPage(py)
