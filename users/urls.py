from django.conf.urls import url
from .views import *
app_name = 'users'
urlpatterns = [
    # url(r'^demo/$', demo, name='demo'),

    url(r'^$', login, name='home'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^add/$', add_user, name='add_user'),
    url(r'^list/', list_user, name='list_user'),

    url(r'^roles/$', roles_list, name='list_roles'),

    ]