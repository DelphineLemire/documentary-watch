import pytest

from contributions.models import Contribution, Topic
from contributions.tests.factories import ContributionFactory, TopicFactory
from contributors.models import Contributor
from contributors.tests.factories import ContributorFactory
from users.models import User
from users.tests.factories import UserFactory
from various.models import Theme
from various.tests.factories import ThemeFactory


@pytest.fixture
def topic(db) -> Topic:
    return TopicFactory()


@pytest.fixture
def contribution(db) -> Contribution:
    return ContributionFactory()


@pytest.fixture
def theme(db) -> Theme:
    return ThemeFactory()


@pytest.fixture
def contributor(db) -> Contributor:
    return ContributorFactory()


@pytest.fixture
def user(db) -> User:
    return UserFactory()
