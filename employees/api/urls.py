from django.urls import path
from employees.api.views import DepartmentCreateReadApi,DepartmentUpdateApi,DepartmentDestroyAPIView,PositionCreateApiView,PositionRetrieveCreateApiView,PositionDestroyAPIView,EmployeeCreateApiView,EmployeeDestroyAPIView,EmployeeReitiveUpdateApiView

urlpatterns = [
    path("department/",DepartmentCreateReadApi.as_view(),name = "department"),
    path("department/<int:pk>/",DepartmentUpdateApi.as_view(),name = "update_department"),
    path("remove/department/<int:pk>/",DepartmentDestroyAPIView.as_view(),name = "delete_department"),
    path("position/",PositionCreateApiView.as_view(),name = "position"),
    path("position/<int:pk>/",PositionRetrieveCreateApiView.as_view(),name =  "position_get_update"),
    path("remove/position/<int:pk>/",PositionDestroyAPIView.as_view(),name =  "position_delete"),
    path("employee/",EmployeeCreateApiView.as_view(),name = "employee"),
    path("employee/<int:pk>/",EmployeeReitiveUpdateApiView.as_view(),name = "employee"),
    path("remove/employee/<int:pk>/",EmployeeDestroyAPIView.as_view(),name = "employee_delete"),
]