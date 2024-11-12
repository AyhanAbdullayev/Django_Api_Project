from rest_framework import serializers
from accounts.models import User


class UserSerializers(serializers.ModelSerializer):

    # username = serializers.CharField(read_only = True)


    class Meta:
        model = User
        fields = ["id","username","password","email","first_name","last_name","is_staff","is_active"]


    

    # def validate(self,data):
    #     context = self.context['request']
    #     data['username'] = context.user
    #     return data 

    




    