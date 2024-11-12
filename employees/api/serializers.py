from rest_framework import serializers
from employees.models import Department,Position,Employee
from django.utils.translation import gettext_lazy as _

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ["id","name","created_at","updated_at"]

    



    
        





class PositionSerializer(serializers.ModelSerializer):


    class Meta:
        model = Position
        fields = ["id","name","salary","department_id","created_at","updated_at"]




class EmployeeSerializer(serializers.ModelSerializer):


    class Meta:
        model = Employee
        fields = ["id","name","surname","email","department_id","position_id","status","created_at","updated_at"]

