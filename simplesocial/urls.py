from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', views.Homepage.as_view(), name='home'),
    #this is allow us to connect that django has for authrisation
    path('accounts/', include('django.contrib.auth.urls')),
    path('test/', views.TestPage.as_view(), name='test'),
    path('froala_editor/',include('froala_editor.urls')),
    path('thanks/', views.ThanksPage.as_view(), name='thanks'),
    path('posts/', include('posts.urls', namespace='posts')),
    path('groups/', include('groups.urls', namespace='groups')),
]
