from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),

]


admin.site.site_header = "Django With CodingForEntrepreneurs"



