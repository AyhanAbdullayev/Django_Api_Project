from modeltranslation.translator  import translator,TranslationOptions
from employees.models import Employee,Department,Position


class EmployeeTranslateOptions(TranslationOptions):
    fields = ("status",)

class DepartmentTranslateOptions(TranslationOptions):
    fields = ("name",)

class PositionTranslateOptions(TranslationOptions):
    fields = ("name",)

translator.register(Employee,EmployeeTranslateOptions)

translator.register(Department,DepartmentTranslateOptions)

translator.register(Position,PositionTranslateOptions)