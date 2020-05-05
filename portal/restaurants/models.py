from django.db import models

class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    cuisines = models.CharField(max_length=100)
    contact_no = models.IntegerField()
    avg_cost_for_a_person = models.IntegerField()
    is_delivering_now = models.BooleanField(default=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.name








# Create your models here.
