from .allrepo import Vehicle_repository, Vehicle_employee_repository, Company_repository, Director_repository, Employee_repository, Race_repository, Route_stop_repository, Stop_repository, Ticket_repository, Route_repository


class Repository_manager:
    def __init__(self):
        self.ticket=Ticket_repository()
        self.vehicle=Vehicle_repository()
        self.company=Company_repository()
        self.director=Director_repository()
        self.employee=Employee_repository()
        self.race=Race_repository()
        self.route_stop=Route_stop_repository()
        self.stop=Stop_repository()
        self.vehicle_employee=Vehicle_employee_repository()
        self.route=Route_repository()

