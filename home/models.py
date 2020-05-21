from django.db import models

from django.core.validators import validate_comma_separated_integer_list


# Create your models here.

class BusInfo(models.Model):
	bus_id = models.IntegerField()
	source = models.CharField(max_length=10)
	destination = models.CharField(max_length=10)
	arrival = models.TimeField()
	departure = models.TimeField()

	def __str__(self):
		return str(self.bus_id)


class Status(models.Model):
	bus_id = models.IntegerField(default=123)
	seats = models.CharField(validators=[validate_comma_separated_integer_list], max_length=200,
							 default='a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a')

	def __str__(self):
		return str(self.bus_id)


class Customer(models.Model):
	ticket_id = models.IntegerField(default=0)
	ticket_booked = models.IntegerField(null=True)
	customer_name = models.CharField(max_length=30, null=True)

	def __str__(self):
		return str(self.ticket_id)

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email


class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid =models.DecimalField(decimal_places=0, max_digits=2)
    busid=models.DecimalField(decimal_places=0, max_digits=2)
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)

    def __str__(self):
        return self.email
