from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name="home"),
    path("home", views.home),
    path("records", views.records, name="records"),
    path("search", views.search,name="search"),
    path("searchkeyword", views.searchkeyword,name="searchkeyword"),
    path("stack", views.stack,name="stack"),
    path("stacksearch", views.stackSearch, name="stacksearch")
]