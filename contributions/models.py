from django.db.models import CASCADE, CharField, ForeignKey, Model
from django.utils.translation import gettext_lazy as _

from various.models import Theme


class Topic(Model):
    """
        Topic of the subject followed.

        """
    label = CharField(_("Label"), max_length=255)
    description = CharField(_("description"),
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
