from django.urls import path
from webapp.views import IndexView, add, subtract, multiply, divide

urlpatterns = [
    path("", IndexView, name='index'),
    path("add/", add, name='add'),
    path("subtract/", subtract, name='subtract'),
    path("multiply/", multiply, name='multiply'),
    path("divide/", divide, name='divide'),
]
