from django.contrib import admin
from django.urls import path,re_path,include
# re_path means regex( regular expression) path
from searches import views as search_views

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('',include('blog.urls')),
    path('about/',include('about.urls')),
    path('contact/',include('contact.urls')),
    path('search/',search_views.search,name='search'),
]
admin.site.site_header = "Django With CodingForEntrepreneurs"

