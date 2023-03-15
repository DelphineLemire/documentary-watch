from factory.django import DjangoModelFactory

from various.models import Theme


class ThemeFactory(DjangoModelFactory):

    label = 'test_label'

    class Meta:
        model = Theme
        django_get_or_create = ["label"]
