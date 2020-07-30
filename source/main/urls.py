"""main URL Configuration

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
from django.contrib import admin
from django.urls import path
from webapp.views import index_view, memo_view, memo_create_view, memo_delete_view, memo_update_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('memo/<int:pk>/', memo_view, name='memo_view'),
    path('memo/add/', memo_create_view, name='memo_create'),
    path('memo/<int:pk>/update/', memo_update_view, name='memo_update'),
    path('memo/<int:pk>/delete/', memo_delete_view, name='memo_delete')
]
