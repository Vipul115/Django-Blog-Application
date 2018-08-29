from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from .views import post_detail,post_update,post_list,post_delete,post_create
urlpatterns = [
    url(r'^$', post_list),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r"^create/$", post_create, name='create'),
    url(r'^update/(?P<id>\d+)/$', post_update),
    url(r'^delete/$', post_delete)

]



#if settings.DEBUG:
#    urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)