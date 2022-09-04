from django.db import models

class Size(models.Model):
    SIZE = [
        ('1', 'Small'),
        ('2', 'Medium'),
        ('3', 'Large'),
    ]
    title = models.CharField('Size', max_length=10, choices=SIZE)

    def __str__(self):
        return self.title # This is for good visual experimentation!

class Pizza(models.Model):
    topping1 = models.CharField(max_length=30)
    topping2 = models.CharField(max_length=30)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)  

    def __str__(self):
        return self.size, self.topping1, self.topping2

