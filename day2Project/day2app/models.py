from django.db import models
# Create your models here.


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    present_address = models. CharField(max_length=150)
    registration_date = models.DateTimeField(auto_now_add=True)
    reg_no = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name} reg {self.id}'
