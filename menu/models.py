from django.db import models


class Food(models.Model):
    APPETIZER = 'Appetizer'
    ENTREE = 'Entree'
    DESSERT = 'Dessert'
    TYPE_OF_FOOD = (
        (APPETIZER, 'Appetizer'),
        (ENTREE, 'Entree'),
        (DESSERT, 'Dessert'),
    )
    item_type = models.CharField(
        max_length=9,
        choices=TYPE_OF_FOOD,
        default=ENTREE,
    )
    item_name = models.CharField(max_length=1000)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.item_type + ' | Name: ' + self.item_name + ' | Price: ' + str(self.price)


class Beverage(models.Model):
    item_name = models.CharField(max_length=1000)
    alcoholic = models.BooleanField(default=False)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.item_name + ' | Alcoholic: ' + str(self.alcoholic) + '| Price: ' + str(self.price)
