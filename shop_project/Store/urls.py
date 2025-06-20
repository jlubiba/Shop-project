from django.urls import path
from . import views

urlpatterns = [
    path("", views.category, name="category"),
    # path("", views.cats, name="categories"),
    # path("<int:pk>", views.cat, name="category"),
    path("<int:pk>", views.category0, name="category"),
]