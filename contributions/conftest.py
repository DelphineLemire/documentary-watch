import pytest

from contributions.models import Topic
from contributions.tests.factories import TopicFactory
from various.models import Theme
from various.tests.factories import ThemeFactory


@pytest.fixture
def topic(db) -> Topic:
    return TopicFactory()


@pytest.fixture
def theme(db) -> Theme:
    return ThemeFactory()
