from django.db.models import CharField, Model, TextField
from django.utils.translation import gettext_lazy as _


class Contributor(Model):
    """
        Contributor who shares information.

        Not to be confused with app users.

        """
    first_name = CharField(_("First Name"), blank=True, max_length=50)
    last_name = CharField(_("Last Name"), blank=True, max_length=50)
    distinction = CharField(_("Distinction"), blank=True, max_length=50)
    note = TextField(_("description"), blank=True, max_length=500)

    def __str__(self) -> str:
        return f"{self.first_name}, {self.last_name}: {self.distinction}"
