from django.contrib import admin
from django.urls import path
from ActivityAnswersSite.views import Home, Games, Questions, Guides, Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('games/', Games.as_view(), name='games'),
    path('questions/', Questions.as_view(), name='questions'),
    path('guides/', Guides.as_view(), name='guides'),
    path('login/', Login.as_view(), name='login'),
]