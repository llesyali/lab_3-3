from django.urls import path
from . import views

urlpatterns = [
    path('vehicles/', views.VehicleListView.as_view(), name='vehicle_list'),
    path('vehicles/<int:pk>/', views.VehicleDetailView.as_view(), name='vehicle_detail'),

    path('vehicles/create/', views.VehicleCreateView.as_view(), name='vehicle_create'),
    path('vehicles/<int:pk>/update/', views.VehicleUpdateView.as_view(), name='vehicle_update'),
    path('vehicles/<int:pk>/delete/', views.VehicleDeleteView.as_view(), name='vehicle_delete'),
    path('api/settlements/', views.settlements_api_list, name='settlements_api_list'),
    path('api/settlements/<int:pk>/delete/', views.settlement_api_delete, name='settlement_api_delete'),
    path('api/people/', views.persons_api_list, name='persons_api_list'),
    path('api/people/<int:pk>/delete/', views.person_api_delete, name='person_api_delete'),
]