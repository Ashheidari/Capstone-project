from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length = 255, db_index = True)
    price = models.DecimalField(max_digits = 6, decimal_places = 2, db_index = True)
    inventory = models.SmallIntegerField(db_index = True)

    def __str__(self) -> str:
        return f"{self.title} : {str(self.price)}"



class Booking(models.Model):
    name = models.CharField(max_length = 255, db_index = True)
    guests = models.SmallIntegerField()
    booking_date = models.DateTimeField()
