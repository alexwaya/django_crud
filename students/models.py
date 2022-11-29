from django.db import models

# Create your models here.
class Stream(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Student(models.Model):
    name = models.CharField(max_length= 50)
    description = models.TextField()
    joindate = models.DateTimeField(auto_now_add = True)
    reg_no = models.CharField(max_length=100, unique=True)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, related_name="students")

    def __str__(self):
        return f'{self.name} reg {self.reg_no}' 