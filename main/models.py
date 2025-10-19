from django.db import models

class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name_company=models.CharField(max_length=70)
    contact = models.CharField(max_length=10)
    email = models.EmailField(blank=True, null=True)
    locality_address = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    house_number = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.name_company} - {self.contact}"

    class Meta:
        managed = False
        db_table = 'company'

    def show_info(self):
        print(f" Компанія: {self.name_company}, контакти: {self.contact};")

class Vehicle(models.Model):
    vehicle_id=models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    license_plate=models.CharField(max_length=8)
    type=models.CharField(max_length=45)
    place_amount=models.IntegerField()

    def __str__(self):
        return f"{self.license_plate} - {self.type}"

    class Meta:
        managed = False
        db_table = 'vehicle'


    @staticmethod
    def right_plate(plate):
        return len(plate) == 8


class Director(models.Model):
    director_id=models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    surname=models.CharField(max_length=45)
    name=models.CharField(max_length=20)
    contact=models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'director'

    def __str__(self):
        return f"{self.company} - {self.name}"

class Employee(models.Model):
    employee_id=models.AutoField(primary_key=True)
    surname=models.CharField(max_length=45)
    name=models.CharField(max_length=20)
    contact=models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'employee'

    def __str__(self):
        return f"{self.employee_id} - {self.name}"

class Vehicle_employee(models.Model):
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    vehicle=models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'vehicle_employee'
        unique_together = ('employee', 'vehicle')

    def __str__(self):
        return f"{self.employee} - {self.vehicle}"

class Route(models.Model):
    route_id=models.AutoField(primary_key=True)
    length=models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'route'

    def __str__(self):
        return f"{self.route_id} - {self.length}"

class Race(models.Model):
    race_id=models.AutoField(primary_key=True)
    route=models.ForeignKey(Route, on_delete=models.CASCADE)
    vehicle=models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    depature_time=models.TimeField()
    arrival_time=models.TimeField()
    regularity_time=models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'race'


class Ticket(models.Model):
    ticket_id=models.AutoField(primary_key=True)
    race=models.ForeignKey(Race, on_delete=models.CASCADE)
    price=models.IntegerField()
    place_number=models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ticket'

    def __str__(self):
        return f"{self.ticket_id} - {self.price}"

class Stop(models.Model):
    stop_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=45)
    locality=models.CharField(max_length=45)
    street=models.CharField(max_length=45)
    house_number=models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stop'

    def __str__(self):
        return f"{self.stop_id} - {self.name}"

class Route_stop(models.Model):
    route=models.ForeignKey(Route, on_delete=models.CASCADE)
    stop=models.ForeignKey(Stop, on_delete=models.CASCADE)
    order_number=models.IntegerField()

    class Meta:
        managed = False
        db_table = 'route_stop'
        unique_together = ('route', 'stop')




