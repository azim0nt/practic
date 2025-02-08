from django.urls import path
from .views import employees, new_employee

urlpatterns = [
    path('', employees, name='employees'),
    path('add-employee/', new_employee, name='add_employee')
]
