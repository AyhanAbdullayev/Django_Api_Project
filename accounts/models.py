from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def save(self, *args, **kwargs):
        if  not self.password.startswith("pbkdf2_sha256"):
            self.set_password(self.password)
        super().save(*args,**kwargs)



    class Meta:
        verbose_name_plural = "Users"
        verbose_name = "User"




class BlackListIpAdress(models.Model):
    ip_adress = models.GenericIPAddressField()


    class Meta:
        verbose_name_plural = "BlackListIpAdresses"
        verbose_name = "BlackListIpAdress"


    def __str__(self):
        return  f"{self.ip_adress}"



