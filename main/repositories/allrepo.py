from main.models import Route, Stop, Company, Route_stop, Director, Employee, Race, Vehicle_employee, Vehicle, Ticket
from main.repositories.baserepo import BaseRepository


class Route_stop_repository(BaseRepository):
    def __init__(self):
        super().__init__(Route_stop)

class Route_repository(BaseRepository):
    def __init__(self):
        super().__init__(Route)

class Stop_repository(BaseRepository):
    def __init__(self):
        super().__init__(Stop)

class Company_repository(BaseRepository):
    def __init__(self):
        super().__init__(Company)

class Director_repository(BaseRepository):
    def __init__(self):
        super().__init__(Director)

class Employee_repository(BaseRepository):
    def __init__(self):
        super().__init__(Employee)

class Race_repository(BaseRepository):
    def __init__(self):
        super().__init__(Race)

class Vehicle_employee_repository(BaseRepository):
    def __init__(self):
        super().__init__(Vehicle_employee)

class Vehicle_repository(BaseRepository):
    def __init__(self):
        super().__init__(Vehicle)

class Ticket_repository(BaseRepository):
    def __init__(self):
        super().__init__(Ticket)