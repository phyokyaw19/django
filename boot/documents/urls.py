from django.urls import include, path
from . import views

app_name = 'documents'
urlpatterns = [
    path('document_master/list', views.show_dm,  name="show_dm"),
    path('document_master/create/', views.document_master_create.as_view(),  name="document_master_create"),
    path('document_master/<int:pk>/detail/', views.document_master_detail.as_view(),  name="document_master_detail"),
    path('document_master/<int:pk>/update/', views.document_master_update.as_view(),  name="document_master_update"),
    path('document_master/<int:pk>/delete/', views.document_master_delete.as_view(),  name="document_master_delete"),

    path('external_doc/list/', views.external_doc_list,  name="external_doc_list"),
    path('external_doc/create/', views.external_doc_create.as_view(),  name="external_doc_create"),
    path('external_doc/<int:pk>/detail/', views.external_doc_detail.as_view(),  name="external_doc_detail"),
    path('external_doc/<int:pk>/update/', views.external_doc_update.as_view(),  name="external_doc_update"),
    path('external_doc/<int:pk>/delete/', views.external_doc_delete.as_view(),  name="external_doc_delete"),
]
