import pytest

from pages.kyber_pages import KyberPages


@pytest.fixture
def kyber(py):
    return KyberPages(py)
