from django.urls import include, path
from . import views

app_name = 'documents'
urlpatterns = [
    path('document_master/', views.show_dm,  name="show_dm"),
]
