from django.db import models

class Pizza(models.Model):
    topping1 = models.CharField(("Topping One"), max_length=50)
    topping2 = models.CharField(("Topping Two"), max_length=50)
    SIZES = (
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large"),
    )
    size = models.CharField((""), max_length=50, choices=SIZES)



    def __str__(self):
        return f"{self.topping1}, {self.topping2}, {self.size}"