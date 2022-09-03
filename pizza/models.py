from django.db import models

class Pizza(models.Model):
    topping_one = models.CharField(("Topping One"), max_length=50)
    topping_two = models.CharField(("Topping Two"), max_length=50)
    SIZES = (
        ("1", "Small"),
        ("2", "Medium"),
        ("3", "Large"),
    )
    size = models.CharField((""), max_length=50, choices=SIZES)



    def __str__(self):
        return f"{self.topping_one}, {self.topping_two}, {self.size}"