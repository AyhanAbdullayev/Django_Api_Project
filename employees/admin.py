from django.contrib import admin
from employees.models import Department,Position,Employee
from modeltranslation.admin import  TranslationAdmin

@admin.register(Department)
class DepartmentAdmin(TranslationAdmin):
    list_display = ["id","name","created_at","updated_at"]
    list_display_links = ["id","name"]




@admin.register(Position)
class PositionAdmin(TranslationAdmin):
    list_display = ["id","name","salary","department_id","created_at","updated_at"]
    list_display_links = ["id","name","department_id"]





@admin.register(Employee)
class EmployeeAdmin(TranslationAdmin):
    list_display = ["id","name","surname","email","department_id","position_id","status","created_at","updated_at"]
    list_display_links  = ["id","name","email","department_id","position_id"]


