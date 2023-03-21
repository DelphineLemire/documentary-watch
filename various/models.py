from django.db.models import CharField, Model
from django.utils.translation import gettext_lazy as _


class Theme(Model):
    """
        Theme of the topics followed.

        """
    label = CharField(_("Label"), max_length=255)

    def __str__(self):
        return f"{self.label}"

    class Meta:
        verbose_name = _('Theme')
        verbose_name_plural = _('Themes')
