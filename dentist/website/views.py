from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def home(request):
	return render(request,'website/home.html',{}) 

def contact(request):
	if request.method=="POST":
		message_name=request.POST['message-name']
		message_email=request.POST['message-email']
		message=request.POST['message']

		send_mail(
			"for dentist"+ message_name,#subject
			message,#smessage
			message_email,# for email
			['muntasirornob@gmail.com'],# for email
			)
		return render(request,'website/contact.html',{'message_name':message_name})
	else:
		return render(request,'website/contact.html',{}) 


def connect(request):
	if request.method=="POST":
		your_name=request.POST['your-name']
		your_phone=request.POST['your-phone']
		your_email=request.POST['your-email']
		your_address=request.POST['your-address']
		your_scheldule=request.POST['your-scheldule']
		your_time=request.POST['your-time']

		return render(request,'website/connect.html',{
			'your_name' : your_name,
			'your_phone':your_phone,	
			'your_email' : your_email,
			'your_address' : your_address,
			'your_scheldule' : your_scheldule,
			'your_time' : your_time

			})
	else:
		return render(request,'website/home.html',{}) 