from django.utils.deprecation import MiddlewareMixin
from accounts.models import BlackListIpAdress
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _





class BlockListedIpAdress(MiddlewareMixin):

    def process_request(self,request):
        ip = request.META.get("REMOTE_ADDR")
        check_ip = BlackListIpAdress.objects.filter(ip_adress = ip).exists()
        if check_ip:
            translation = (_("You are blocked from this site"))
            return HttpResponse(translation)