from django.urls import include, path
from . import views

app_name = 'documents'
urlpatterns = [
# Document Master List
    path('document_master/list_compact', views.list_compact,  name="list_compact"),
    path('document_master/list', views.show_dm,  name="show_dm"),
    path('document_master/show_dm_print_view', views.show_dm_print_view,  name="show_dm_print_view"),
    path('document_master/create/', views.document_master_create.as_view(),  name="document_master_create"),
    path('document_master/<int:pk>/detail/', views.document_master_detail.as_view(),  name="document_master_detail"),
    path('document_master/<int:pk>/update/', views.document_master_update.as_view(),  name="document_master_update"),
    path('document_master/<int:pk>/delete/', views.document_master_delete.as_view(),  name="document_master_delete"),
# External Document List
    path('external_doc/list/', views.external_doc_list,  name="external_doc_list"),
    path('external_doc/list_print/', views.external_doc_list_print,  name="external_doc_list_print"),
    path('external_doc/create/', views.external_doc_create.as_view(),  name="external_doc_create"),
    path('external_doc/<int:pk>/detail/', views.external_doc_detail.as_view(),  name="external_doc_detail"),
    path('external_doc/<int:pk>/update/', views.external_doc_update.as_view(),  name="external_doc_update"),
    path('external_doc/<int:pk>/delete/', views.external_doc_delete.as_view(),  name="external_doc_delete"),
# DAR
    path('dar/list/', views.dar_list,  name="dar_list"),
    path('dar/list_print/', views.dar_list_print,  name="dar_list_print"),
    path('dar/create/', views.dar_create.as_view(),  name="dar_create"),
    path('dar/<int:pk>/detail/', views.dar_detail.as_view(),  name="dar_detail"),
    path('dar/<int:pk>/update/', views.dar_update.as_view(),  name="dar_update"),
    path('dar/<int:pk>/delete/', views.dar_delete.as_view(),  name="dar_delete"),
]
