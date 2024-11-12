from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Datetime(models.Model):
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)

        
    

class Department(Datetime):
    name = models.CharField(max_length= 200)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name_plural = "Departments"
        verbose_name = "Department"



class Position(Datetime):
    name = models.CharField(max_length = 200)
    salary = models.IntegerField()
    department_id = models.ForeignKey(Department,on_delete = models.SET_NULL,null = True,blank = True )

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name_plural = "Positions"
        verbose_name = "Position"
    


class Employee(Datetime):

    status_choices = [
        ("Active","Active"),
        ("Retired","Retired"),
        ("Leave of Absence","Leave of Absence"),
        ("Fəal","Fəal"),
        ("İşləmir","İşləmir"),
        ("Məzuniyyətə çıxıb","Məzuniyyətə çıxıb"),
    ]


    name = models.CharField(max_length = 200)
    surname = models.CharField(max_length = 200)
    email = models.EmailField(unique = True)
    department_id = models.ForeignKey(Department,on_delete = models.SET_NULL, null = True,blank = True)
    position_id = models.ForeignKey(Position,on_delete = models.SET_NULL,null = True,blank = True)
    status = models.CharField(choices = status_choices,null = True,blank = True,max_length = 200)

    def __str__(self):
        return f"{self.name},{self.surname},{self.email},{self.status}"
    

    class Meta:
        verbose_name_plural = "Employees"
        verbose_name  =  "Employee"

