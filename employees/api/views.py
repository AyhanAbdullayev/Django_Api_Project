from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView
from employees.api.serializers import DepartmentSerializer,PositionSerializer,EmployeeSerializer
from employees.models import Department,Position,Employee
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import NotFound,MethodNotAllowed

class DepartmentCreateReadApi(ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset =  Department.objects.all()
    allowed_methods = ["GET","POST"]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "POST":
            self.serializer_class = DepartmentSerializer
        return self.serializer_class
    
    
    



class DepartmentUpdateApi(RetrieveUpdateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    allowed_methods = ["GET","PUT","PATCH"]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            department_id = Department.objects.get(id=self.kwargs["pk"])
            return department_id 
        except Department.DoesNotExist:
            raise NotFound(detail=_("No Department matches the given query."))
        

        
    





class DepartmentDestroyAPIView(RetrieveDestroyAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    allowed_methods = ["DELETE"]
    permission_classes = [IsAdminUser]

    
    def get_object(self):
        try:
            department_id = Department.objects.get(id=self.kwargs["pk"])
            return department_id 
        except Department.DoesNotExist:
              raise NotFound(detail=_("No Department matches the given query."))
        


        




class PositionCreateApiView(ListCreateAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()
    allowed_methods = ["GET","POST"]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "POST":
            self.serializer_class = PositionSerializer
        return self.serializer_class
    

class PositionRetrieveCreateApiView(RetrieveUpdateAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()
    allowed_methods = ["GET","PUT","PATCH"]
    permission_classes = [IsAuthenticated]


    
    def get_object(self):
        try:
            department_id = Department.objects.get(id=self.kwargs["pk"])
            return department_id 
        except Department.DoesNotExist:
            raise NotFound(detail=_("No Department matches the given query."))




class PositionDestroyAPIView(RetrieveDestroyAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()
    allowed_methods = ["DELETE"]
    permission_classes = [IsAdminUser]


    def get_object(self):
        try:
            department_id = Department.objects.get(id=self.kwargs["pk"])
            return department_id 
        except Department.DoesNotExist:
            raise NotFound(detail=_("No Department matches the given query."))


class EmployeeCreateApiView(ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    allowed_methods = ["GET","POST"]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "POST":
            self.serializer_class = EmployeeSerializer
        return self.serializer_class
    

class EmployeeReitiveUpdateApiView(RetrieveUpdateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    allowed_methods = ["GET","PUT","PATCH"]
    permission_classes = [IsAuthenticated]

    
    def get_object(self):
        try:
            department_id = Department.objects.get(id=self.kwargs["pk"])
            return department_id 
        except Department.DoesNotExist:
            raise NotFound(detail=_("No Department matches the given query."))

    

class EmployeeDestroyAPIView(RetrieveDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    allowed_methods = ["DELETE"]
    permission_classes = [IsAdminUser]


    
    def get_object(self):
        try:
            department_id = Department.objects.get(id=self.kwargs["pk"])
            return department_id 
        except Department.DoesNotExist:
            raise NotFound(detail=_("No Department matches the given query."))
        

