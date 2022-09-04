from django.db import models

# class Pizza(models.Model):
#     topping_one = models.CharField(("Topping One"), max_length=50)
#     topping_two = models.CharField(("Topping Two"), max_length=50)
#     SIZES = (
#         ("1", "Small"),
#         ("2", "Medium"),
#         ("3", "Large"),
#     )
class Size(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        
        return self.title # This is for good visual experimentation!

class Pizza(models.Model):
    topping1 = models.CharField(max_length=100)
    topping2 = models.CharField(max_length=100)
    size = models.ForeignKey(Size, on_delete=models.CASCADE) # This is for correlation to the Size class
    
    def __str__(self):
        return self.size, self.topping1, self.topping2