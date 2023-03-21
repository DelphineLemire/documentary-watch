from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class VariousConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'various'
    verbose_name = _('Various')
