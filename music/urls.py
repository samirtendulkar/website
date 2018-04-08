from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # music/
    url(r'^$', views.AlbumView.as_view(), name='index'),

    #music/register/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # music/712/
    url(r'^(?P<pk>[0-9]+)/$', views.AlbumDetail.as_view(), name='detail'),

    # music/add_album/
    url(r'^add_album/$', views.AlbumCreate.as_view(), name='add_album'),

    # music/712/album_edit/
    url(r'^(?P<pk>[0-9]+)/album_edit/$', views.AlbumUpdate.as_view(), name='album_edit'),

    # music/712/album_delete/
    url(r'^(?P<pk>[0-9]+)/album_delete/$', views.AlbumDelete.as_view(), name='album_delete'),

]

