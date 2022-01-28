from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from contact.forms import ContactForm
from website.settings import RECIPIENT_ADDRESS
 
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            phone = form.cleaned_data['phone']
            company = form.cleaned_data['company']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail('Ny kontakt til Xperta: ' + subject, 'Firma: ' + company + '\nNavn: ' + name + '\nEmail: ' + from_email + '\nTelefon nummer: ' + phone + '\nBesked: ' + message, from_email, [RECIPIENT_ADDRESS])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.info(request, 'Mange tak for din besked. Vi vender tilbage så hurtigt som muligt!')
            return HttpResponseRedirect("/")
    else:
        form = ContactForm()
    
    return render(request, "mainsite/index.html", {'form': form})

def successView(request):
    messages.info(request, 'Mange tak for din besked. Vi vender tilbage så hurtigt som muligt!')
    return HttpResponseRedirect("mainsite/index.html")

def services(request):
    return render(request, 'mainsite/services.html')

def about(request):
    return render(request, 'mainsite/about.html')