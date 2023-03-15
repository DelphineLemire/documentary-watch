from factory.django import DjangoModelFactory

from contributions.models import Topic


class TopicFactory(DjangoModelFactory):

    label = 'test_label'

    class Meta:
        model = Topic
        django_get_or_create = ["label"]
