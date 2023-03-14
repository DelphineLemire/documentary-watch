import pytest

from .models import Contributor
from .tests.factories import ContributorFactory


@pytest.fixture
def contributor(db) -> Contributor:
    return ContributorFactory()
