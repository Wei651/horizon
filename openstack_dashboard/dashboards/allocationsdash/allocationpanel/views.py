from horizon import tabs
from openstack_dashboard.dashboards.allocationsdash.allocationpanel import tabs as alloc_tabs

class IndexView(tabs.TabbedTableView):
    tab_group_class = alloc_tabs.AllocationpanelTabs
    # A very simple class-based view...
    template_name = 'allocationsdash/allocationpanel/index.html'

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
        return context
