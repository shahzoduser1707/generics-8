from django.urls import path
from .views import GetMusic,CreateMusic,GetCreateMusic,DetailUpdateDestroy

urlpatterns = [
    path('getMusic/',GetMusic.as_view()),
    path('createMusic/',CreateMusic.as_view()),
    path('getcreateMusic/',GetCreateMusic.as_view()),
    path('<int:pk>/',DetailUpdateDestroy.as_view())
]