from django.db import models
import enum
# Create your models here.

class Berth_Preferences(enum.Enum):
    L = 1
    M = 2
    U = 3


class Passenger():
    def __init__(self, name: str, age: int, senior_citizen: bool, berth_preference: Berth_Preferences):
        self.name = name
        self.age = age
        self.senior_citizen = senior_citizen
        self.berth_preference = berth_preference



class Database(models.Model):
    boarding_place = models.CharField(max_length=100)
    destination_place = models.CharField(max_length=100)
    date_of_travel = models.DateField()
    passenger_name = models.CharField(max_length=100)
    passenger_age = models.IntegerField('Age')
    passenger_senior_citizen = models.BooleanField('Is Senior Citizen')
    passenger_berth_preference = models.CharField(
        max_length=1,
        default='Lower',
        choices=[
            (Berth_Preferences.L, ('Lower')),
            (Berth_Preferences.M, ('Middle')),
            (Berth_Preferences.U, ('Upper')),
        ],
    )
