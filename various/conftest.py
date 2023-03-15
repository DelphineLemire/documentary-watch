import pytest

from various.models import Theme
from various.tests.factories import ThemeFactory


@pytest.fixture
def theme(db) -> Theme:
    return ThemeFactory()
