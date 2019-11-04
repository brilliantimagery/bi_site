"""bi_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from . import views
from .views import PostCreateView, PostDeleteView, PostDetailView, PostUpdateView

app_name = 'post'

urlpatterns = [
    path('', views.category_view, name='category-view'),
    path('new/', PostCreateView.as_view(), name='create-view'),
    path('<slug:slug_series>/', views.series_view, name='series-view'),
    path('<slug:slug_series>/<slug:slug_post>/', PostDetailView.as_view(), name='detail-view'),
    path('<slug:slug_series>/<slug:slug_post>/delete/', PostDeleteView.as_view(), name='delete-view'),
    path('<slug:slug_series>/<slug:slug_post>/update/', PostUpdateView.as_view(), name='update-view'),
]