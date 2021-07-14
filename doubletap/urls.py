from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns=[
    url(r'^$',views.index, name='index'),
    url('register/',views.register, name='registration'),
    url('login/',auth_views.LoginView.as_view(), name='login'),
    url('logout/',auth_views.LogoutView.as_view(),name='logout'),
    url('profile/',views.insta_profile, name='profile'),
    url('Update_insta_Profile/',views.Update_insta_Profile, name='update_profile'),
    url('search/', views.search_profile,name='search'),
    url(r'^new/image$', views.Post_gram, name='newpost'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
