from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BooksList.as_view(), name='Home'),
    path('<int:pk>/issue/', views.IssueBook.as_view(), name='IssueBook'),
    path('<int:pk>/return/', views.ReturnBook.as_view(), name='ReturnBook'),
]