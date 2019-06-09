from django.conf.urls import url
from .views import *
app_name = 'employeeRequest'
urlpatterns = [
    # url(r'^demo/$', demo, name='demo'),
    url(r'^add_request/$', add_request, name='add_request'),
    url(r'^request_list/$', list_request, name='list_request'),
    url(r'^edit_request/(?P<req_id>[0-9]+)/$', edit_request, name='edit_request'),
    url(r'^edit_request_status/(?P<req_id>[0-9]+)/$', edit_request_status, name='edit_request_status'),
    url(r'^pdf_view/$', pdf_view, name='pdf_view'),
]