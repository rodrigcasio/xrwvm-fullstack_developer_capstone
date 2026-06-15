from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name  # Return the name as the string representation



# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    dealer_id = models.IntegerField()  # <- instructions asked this missing field
    name = models.CharField(max_length=100)
    
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    
    # Updated default to 2026 and MaxValueValidator to 2026 to avoid validation errors
    year = models.IntegerField(default=2026,
        validators=[
            MaxValueValidator(2026),
            MinValueValidator(2015)
        ])

    def __str__(self):
        return self.car_make.name + " " + self.name  # Returns full name (e.g. "Toyota Corolla")

