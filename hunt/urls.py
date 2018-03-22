from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url(r'^home/$',views.home,name = 'home'),
    url(r'^contact/$', views.contact, name= 'contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^new_house/$', views.new_house, name='new_house'),
    url(r'^search/$', views.search_results, name='search_results'),
    url(r'^house_details/(?P<id>\d+)/$', views.house_details, name='house_details'),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)