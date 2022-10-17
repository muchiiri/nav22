from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import SeaFreightShip
from accounts.models import Account
from django.core.mail import send_mail
from django.conf import settings

#quote creation signal
@receiver(post_save, sender=SeaFreightShip)
def quote_creation(sender, instance, created, **kwargs):
    if created:
        owner = instance.owner
        #get users in particular group
        users = Account.objects.filter(groups__name='Ogl_fielduser')
        #get email of users
        user_emails = [user.email for user in users]
        #join owner and users emails
        email_recipients = [owner] + user_emails

        subject = 'Sea Shipment Created'
        message = f'Hi,a shipment for {instance.owner} has been created'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = email_recipients
        
        send_mail( subject, message, email_from, recipient_list, fail_silently=True )
        print("New shipment Created")