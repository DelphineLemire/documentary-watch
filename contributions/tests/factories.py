from factory.django import DjangoModelFactory

from contributions.models import Contribution, Topic


class TopicFactory(DjangoModelFactory):

    label = 'test_label'

    class Meta:
        model = Topic
        django_get_or_create = ["label"]


class ContributionFactory(DjangoModelFactory):

    resume = 'test_resume'

    class Meta:
        model = Contribution
        django_get_or_create = ["resume"]
