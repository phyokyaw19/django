from django.urls import include, path
from . import views

app_name = 'check'
urlpatterns = [
    path('', views.check_view,  name="check"),
    path('addstaff/', views.add_staff,  name="add_staff"),
    path('liststaff/', views.list_staff,  name="list_staff"),
    path('liststaff/<slug:slug>/', views.detail_staff,  name="detail_staff"),

]