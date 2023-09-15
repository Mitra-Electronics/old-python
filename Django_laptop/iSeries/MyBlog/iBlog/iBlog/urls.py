from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('blog/', include('blog.urls')),
    path('', views.home, name='home'),
    #path('services/', include('services.urls')),

]
