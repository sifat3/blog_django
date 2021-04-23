from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('article/<int:pk>', views.ArticleView.as_view(), name='article')
]
