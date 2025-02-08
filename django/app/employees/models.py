from django.db import models


class Employees(models.Model):
    ROLE_CHOICES = [
        ('Backend', 'Backend'),
        ('Frontend', 'Frontend'),
        ('Fullstack', 'Fullstack'),
        ('DevOps', 'DevOps'),
        ('MobileDev', 'MobileDev'),
    ]
    
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'
        
    def __str__(self):
        return self.name