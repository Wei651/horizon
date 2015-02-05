from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.allocationsdash import dashboard

class Allocationpanel(horizon.Panel):
    name = _("Allocation")
    slug = "allocationpanel"


dashboard.Allocationsdash.register(Allocationpanel)
