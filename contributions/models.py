from django.db.models import CASCADE, CharField, ForeignKey, Model, TextField
from django.utils.translation import gettext_lazy as _

from contributors.models import Contributor
from various.models import Theme


class Topic(Model):
    """
        Topic followed.

        """
    label = CharField(_("Label"), max_length=255)
    description = TextField(_("description"),
                            null=True,
                            blank=True,
                            max_length=255)
    theme = ForeignKey(Theme,
                       related_query_name='theme',
                       null=True,
                       blank=True,
                       related_name="topics",
                       on_delete=CASCADE)

    def __str__(self):
        return f"{self.label}"

    class Meta:
        verbose_name = _('Topic')
        verbose_name_plural = _('Topics')


class Contribution(Model):
    """
        Topic followed.

        """
    resume = CharField(_("resume"), max_length=255)
    contributor = ForeignKey(Contributor,
                             related_query_name='contributor',
                             null=True,
                             blank=True,
                             related_name="contributions",
                             on_delete=CASCADE)

    url = CharField(_("url"), max_length=255)
    topic = ForeignKey(Topic,
                       related_query_name='topic',
                       null=True,
                       blank=True,
                       related_name="contributions",
                       on_delete=CASCADE)

    def __str__(self):
        return f"{self.contributor}/{self.resume}"

    class Meta:
        verbose_name = _('Contribution')
        verbose_name_plural = _('Contributions')
