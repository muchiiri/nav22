# code
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Quote, Quote_App
from accounts.models import Account
from django.core.mail import send_mail
from django.conf import settings

#quote creation signal
@receiver(post_save, sender=Quote_App)
def send_email_quote_creation(sender, instance, created, **kwargs):
    if created:
        owner = instance.owner.email
        #get users in particular group
        users = Account.objects.filter(groups__name='Ogl_fielduser')
        #get email of users
        user_emails = [user.email for user in users]
        #join owner and users emails
        email_recipients = [owner] + user_emails

        subject = 'Quote Created'
        message = f'Hi,a quote for {instance.owner.firstname} {instance.owner.lastname} has been created'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = email_recipients
        
        send_mail( subject, message, email_from, recipient_list, fail_silently=True )
        print("New Quote Created")

#quote approval signal
@receiver(post_save, sender=Quote_App)
def send_email_quote_approval(sender, instance, created, **kwargs):
    if instance.status == "review":
        owner = instance.owner.email
        #get users in particular group
        users = Account.objects.filter(groups__name='Admins')
        #get email of users
        user_emails = [user.email for user in users]
        #join owner and users emails
        email_recipients = user_emails

        subject = 'Quote Pricing'
        message = f'Hi,a quote for {instance.owner.firstname} {instance.owner.lastname} has been reviewed, awaiting your approval'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = email_recipients
        
        send_mail( subject, message, email_from, recipient_list, fail_silently=True )
        print("Quote Pricing")

#quote admin approval signal
#send to client
@receiver(post_save, sender=Quote_App)
def send_email_quote_approval_admin(sender, instance, created, **kwargs):
    if instance.status == "approved_admin":
        owner = instance.owner.email
        email_recipients = [owner]

        subject = 'Quote Approved'
        message = f'Hi,{instance.owner.firstname} {instance.owner.lastname}, your quote has been approved. Awaiting your approval'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = email_recipients
        
        send_mail( subject, message, email_from, recipient_list, fail_silently=True )
        print("Quote Approved by admin")

#quote client approval signal
@receiver(post_save, sender=Quote_App)
def send_email_quote_approval_client(sender, instance, created, **kwargs):
    if instance.status == "approved_client":
        owner = instance.owner.email
        #get users in particular group
        users = Account.objects.filter(groups__name='Ogl_fielduser')
        #get email of users
        user_emails = [user.email for user in users]
        #join owner and users emails
        email_recipients = [owner] + user_emails

        subject = 'Quote Approved by Client'
        message = f'Dear Sir/Madam, the quote for {instance.owner.firstname} {instance.owner.lastname}, has has been approved by the client.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = email_recipients
        
        send_mail( subject, message, email_from, recipient_list, fail_silently=True )
        print("Quote Approved by client")