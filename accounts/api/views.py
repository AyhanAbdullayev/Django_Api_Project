from accounts.models import User
from accounts.api.serializers import UserSerializers
from rest_framework.generics import ListCreateAPIView


class UserListCreateApiView(ListCreateAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()
    allowed_methods = ["GET","POST"]
    
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            self.serializer_class = UserSerializers
        return self.serializer_class
    

    



    

    
    