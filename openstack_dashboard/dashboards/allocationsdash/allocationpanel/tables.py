from django.utils.translation import ugettext_lazy as _

from horizon import tables

class InstancesTable(tables.DataTable):
    name = tables.Column("name", verbose_name = ("Project Name"))
    status = tables.Column("status", verbose_name = ("Status"))
    pi = tables.Column("pi", verbose_name = ("PI"))

    class Meta:
        name = "instances"
        verbose_name = _("Instances")

