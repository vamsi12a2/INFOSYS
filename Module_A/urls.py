from . import views
from django.conf.urls import url


urlpatterns =[
    url(r'/index',views.index_view,{}),
]