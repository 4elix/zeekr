from django.urls import path
from .views import NewsList, NewsDetail

urlpatterns = [
    path('list/', NewsList.as_view()),
    path('detail/<slug:slug>/', NewsDetail.as_view())
]