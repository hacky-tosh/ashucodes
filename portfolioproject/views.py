from django.shortcuts import render
from portfolioproject.models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


#from ipware import    name = request.POST.get('name')
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        ins = Contact(name=name, email=email, subject=subject,message=message)
        ins.save()
        messages.success(request, 'Your message has been sent')

       # mail_subject = 'ashu.codes'
      #  mail_message = f"Name: {name} \n email: {email} \n subject: {subject} \n message: {message} \n"
     #   email_from = settings.EMAIL_HOST_USER
    #    recipient_list = ['bankashu74@gmail.com', ]
   #     send_mail(mail_subject,mail_message, email_from, recipient_list)

    return render(request,'index.html')

 #   if request.method == 'GET':
  #     ip, is_routeble = get_client_ip(request)
   #    if ip is None:
 #          ip = '0.0.0.0'
#       else:
  #         if is_routeble:
   #            ipv = 'Public'
    #       else:
     #          ipv = 'Private'

      # mail_subject = 'Ashu Website view'
      # mail_message = f'someone opened your website  from {ip} that is {ipv} '
      # email_from = settings.EMAIL_HOST_USER
      # recipient_list = ['bankashu74@gmail.com', ]
       #send_mail(mail_subject,mail_message,email_from,recipient_list)





    #return render(request, 'index.html')




def hehe(request):
   # if request.method == 'GET':
      #  ip, is_routeble = get_client_ip(request)
      #  if ip is None:
        #    ip = '0.0.0.0'
       # else:
           # if is_routeble:
          #      ipv = 'Public'
         #   else:
        #        ipv = 'Private'

       # mail_subject = 'Ashu Website view'
        #mail_message = f'someone opened your website root from {ip} that is {ipv} '
       # email_from = settings.EMAIL_HOST_USER
        #recipient_list = ['maxd20506@gmail.com', ]
       # send_mail(mail_subject,mail_message,email_from,recipient_list)  
    return render(request, 'r00t.html')

