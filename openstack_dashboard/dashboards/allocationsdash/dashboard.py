from django.utils.translation import ugettext_lazy as _

import horizon

class Allocationgroup(horizon.PanelGroup):
    slug = "allocationgroup"
    name = _("My Allocations")
    panels = ('allocationpanel',)


class Allocationsdash(horizon.Dashboard):
    name = _("Allocations")
    slug = "allocationsdash"
    panels = (Allocationgroup,)  # Add your panels here.
    default_panel = 'allocationpanel'  # Specify the slug of the dashboard's default panel.


horizon.register(Allocationsdash)
