from celery import shared_task
from accounts.models import User
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from Web_Employ import settings

@shared_task
def send_mail_task():
    users = User.objects.all()

    if users:
        for user in users:

            last_login = user.last_login

            data_joined = user.date_joined

            delta = (last_login - data_joined )

            delta_hours =  delta.total_seconds() / 3600

            if (delta_hours > 48): 
                subject = "Warning Message"
                text_context = "User don't login during 2 or more days."

                email = user.email

                delta_days = delta.days

                message = render_to_string("email-subscribers.html",
                                {"user":user,
                                "email":email,
                                "days":delta_days}) 
                    
                msg = EmailMultiAlternatives(subject,text_context,settings.EMAIL_HOST_USER,[email])
                msg.attach_alternative(message,"text/html")
                msg.send()



