from django.urls import include, path
from . import views

app_name = 'machine'
urlpatterns = [
    path('machine_add/', views.MachineCreate.as_view(),  name="add_machine"),
    path('machine_list/', views.list_machine,  name="list_machine"),
    path('<int:pk>/detail/', views.detail_machine.as_view(),  name="detail_machine"),
    path('<int:pk>/update/', views.update_machine.as_view(),  name="update_machine"),
    path('<int:pk>/delete/', views.delete_machine.as_view(),  name="delete_machine"),
    path('supplier/supplier_add/', views.SuppliersCreate.as_view(),  name="add_supplier"),
    path('supplier/supplier_list/', views.list_supplier,  name="list_supplier"),
    path('supplier/<int:pk>/detail/', views.detail_supplier.as_view(),  name="detail_supplier"),
    path('supplier/<int:pk>/update/', views.update_supplier.as_view(),  name="update_supplier"),
    path('supplier/<int:pk>/delete/', views.delete_supplier.as_view(),  name="delete_supplier"),
]

