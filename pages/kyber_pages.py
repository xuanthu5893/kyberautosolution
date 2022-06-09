from pages.analytics_page import AnalyticsPage
from pages.swap_page import SwapPage
from pages.pool_page import PoolPage


class KyberPages:
    def __init__(self, py):
        self.py = py
        self.swap = SwapPage(py)
        self.pool = PoolPage(py)
        self.analytics = AnalyticsPage(py)
