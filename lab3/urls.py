
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main.views import *

router = routers.DefaultRouter()

router.register(r'vehicle_employee', Vehicle_employeeViewSet, basename='vehicle_employee')
router.register(r'vehicles', VehicleViewSet, basename='vehicle')
router.register(r'races', RaceViewSet, basename='race')
router.register(r'routes', RouteViewSet, basename='route')
router.register(r'companies', CompanyViewSet, basename='company')
router.register('employees', EmployeeViewSet, basename='employee')
router.register('directors', DirectorViewSet, basename='director')
router.register('route_stop', Route_stopViewSet, basename='route_stop')
router.register('stops', StopViewSet, basename='stop')
router.register('tickets', TicketViewSet, basename='ticket')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("api/auth/", include("authentication.urls")),
    path('tickets-report/', TicketReportView.as_view(), name='ticket-report'),
    path('', include('webapp.urls')),

]
