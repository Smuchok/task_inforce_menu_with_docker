from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField()
    password = models.CharField()

    class Meta:
        abstract = True


class Employee(User):
    email = models.EmailField()

    def __str__(self):
        return self.username


class Restaurant(User):
    name = models.CharField()
    addrress = models.CharField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    title = models.CharField()
    price = models.FloatField()
    restaurant = models.ForeignKey('Restaurant',  on_delete=models.SET_NULL, null=True)
    menu = models.JSONField()
    day = models.IntegerField() # use date field too complicated

    def __str__(self):
        return str(self.title) + ' - day ' + str(self.day)
