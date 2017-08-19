from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^view/(?P<pk>\d+)$', views.model_view, name='model_view'),
    url(r'^$', views.formmm, name='formmm'),
    url(r'^api/input/hgb=(?P<hgb>\d+\.\d+)/wbc=(?P<wbc>\d+\.\d+)/age=(?P<age>\d+)/smk=(?P<smk>\d+)/nveg=(?P<nveg>\d+)/occ=(?P<occ>\d+)$', views.predict_out, name='Output'),    
]