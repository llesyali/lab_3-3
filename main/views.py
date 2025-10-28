from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

class  BaseViewSet(viewsets.ModelViewSet):
    repository=None
    serializer_class=None

    def list(self,request):
        data=self.repository.get_all()
        serializer=self.serializer_class(data,many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = self.repository.get_by_id(pk)
        if obj:
            serializer = self.serializer_class(obj)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def  create(self,request):
        new_d=self.repository.create(request.data)
        serializer=self.serializer_class(new_d)
        return Response(serializer.data,status=status.HTTP_201_CREATED)


    def destroy(self,request,pk=None):
        obj=self.repository.delete(pk)
        if obj:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


from main.repositories.repomanager import Repository_manager
from .serializers import *

repo=Repository_manager()

class Route_stopViewSet(BaseViewSet):
    repository=repo.route_stop
    serializer_class=Route_stopSerializer
    queryset=Route_stop.objects.all()

class RouteViewSet(BaseViewSet):
    repository = repo.route
    serializer_class = RouteSerializer
    queryset = Route.objects.all()

class CompanyViewSet(BaseViewSet):
    repository = repo.company
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

class StopViewSet(BaseViewSet):
    repository = repo.stop
    serializer_class = StopSerializer
    queryset = Stop.objects.all()

class EmployeeViewSet(BaseViewSet):
    repository = repo.employee
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class DirectorViewSet(BaseViewSet):
    repository = repo.director
    serializer_class = DirectorSerializer
    queryset = Director.objects.all()

class VehicleViewSet(BaseViewSet):
    repository = repo.vehicle
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()

class TicketViewSet(BaseViewSet):
    repository = repo.ticket
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

class Vehicle_employeeViewSet(BaseViewSet):
    repository = repo.vehicle_employee
    serializer_class = Vehicle_employeeSerializer
    queryset = Vehicle_employee.objects.all()

class RaceViewSet(BaseViewSet):
    repository = repo.race
    serializer_class = RaceSerializer
    queryset = Race.objects.all()


class TicketReportView(APIView):
    def get(self, request):
        tickets = Ticket.objects.all()
        total_tickets = tickets.count()
        total_income = sum(ticket.price for ticket in tickets)

        report = {
            "total_tickets": total_tickets,
            "total_income": total_income,
            "average_price": total_income / total_tickets if total_tickets > 0 else 0
        }

        return Response(report, status=status.HTTP_200_OK)