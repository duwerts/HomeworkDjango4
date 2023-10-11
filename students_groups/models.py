from django.db import models
from pythonпDjangoProject4.students.models import Students
from pythonпDjangoProject4.group.models import Teacher




class Group(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Students)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


