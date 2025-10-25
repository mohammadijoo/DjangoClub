"""pythonclubir URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views
from django.conf.urls import handler404, handler500, handler403, handler400


handler404 = 'views.custom_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('contactEn/', views.contactEn, name='contactEn'),
    path('search_results/', views.search_results, name='search-results'),
    path('search_resultsfa/', views.search_resultsfa, name='search-resultsfa'),
    
    path('', include('social_django.urls', namespace='social')),
    
    path('en/', views.en, name='en'),
    
    path('theblog/', include('theblog.urls')),
    path('theblogfa/', include('theblogfa.urls')),
    path('ml/', include('ml.urls', namespace='ml')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    
    
    
    # path('iris/', views.irisDataset, name='iris'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)





