from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path('', views.BlogList.as_view(), name = 'blog-list'),
    path('<int:pk>/', views.BlogDetail.as_view(), name = 'blog-detail')
]
