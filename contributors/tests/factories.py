from factory.django import DjangoModelFactory

from contributors.models import Contributor


class ContributorFactory(DjangoModelFactory):

    first_name = 'lemire'
    last_name = 'dedel'
    distinction = 'IT developer'

    class Meta:
        model = Contributor
        django_get_or_create = ["first_name", "last_name", "distinction"]
