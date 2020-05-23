from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homepage ,name='homepage'),
    path('blog/', views.post_list_view, name='post-list'),
    path('post/<slug:post_slug>/', views.post_detail_view, name='post-detail'),
    path('post/<slug:post_slug>/update', views.post_update_view, name='post-update'),
    path('post/<slug:post_slug>/delete', views.post_delete_view, name='post-delete'),

    path('post-new/', views.post_create_view, name='post-create'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)