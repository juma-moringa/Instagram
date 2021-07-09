from django.conf.urls import url
from . import views
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.index,name='index'),
    url('register/',views.register, name='registration'),
 
]
