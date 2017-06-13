from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^index/$', views.index_view, {}),
    url(r'^(?P<id>\d+)/$', views.post_view, {}),
    url(r'^create/$', views.user_form, name="createuser"),
    url(r'^(?P<name>\w+)/$', views.name_view,name="byname"),

]