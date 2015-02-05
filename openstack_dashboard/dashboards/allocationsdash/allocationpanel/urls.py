from django.conf.urls import patterns
from django.conf.urls import url

from openstack_dashboard.dashboards.allocationsdash.allocationpanel import views


urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^\?tab=allocationpanel_tabs__tab$', views.IndexView.as_view(), name='allocationpanel_tabs'),
)
