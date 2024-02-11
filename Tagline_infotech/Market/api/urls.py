from django.contrib import admin
from django.urls import path,include
from .views import  UserListView,ProductListView,PurchaseListView,ProductUpdateView,PurchaseUpdateView

urlpatterns = [
    path("user/",UserListView.as_view()),
    path("product/",ProductListView.as_view()),
    path("purchase/",PurchaseListView.as_view()),
    path("product/<int:pk>",ProductUpdateView.as_view()),
    path("purchase/<int:pk>",PurchaseUpdateView.as_view())
]
