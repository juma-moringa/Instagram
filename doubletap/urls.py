from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns=[
    url(r'^$',views.index, name='index'),
    url('register/',views.register, name='registration'),
    url('login/',auth_views.LoginView.as_view(), name='login'),
    url('profile/',views.insta_profile, name='profile'),
    url('Update_insta_Profile/',views.Update_insta_Profile, name='update_profile'),
    url('gramblog/', views.Post_gram, name='Postblog'),
    url('search/', views.search_profile,name='search'),
]
