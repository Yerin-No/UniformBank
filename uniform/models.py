from django.db import models

class Uniform(models.Model):
    name = models.CharField(max_length=20)
    size = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name} : {self.size}'    # 동복치마 : 100