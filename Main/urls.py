from django.urls import path
from .views import home
urlpatterns = [
    # urls here
    path('', home, name='HomeView')
]
