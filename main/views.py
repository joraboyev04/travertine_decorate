import requests
from django.shortcuts import render, redirect
from .models import *

def Photo(request):
    context = {
              'photos' : Pictures.objects.all(),
              'blogs' : Blog.objects.all()

        }
    return render(request,'index-4.html',context)


def Sendmsg(request):

    ism = request.POST['ism']
    manzil = request.POST['manzil']
    phone = request.POST['phone']


    bot_token = '5194924816:AAHsAj38uA7mpBku8cgndiOIjluT_NlIV9M'
    text = 'Saytdan xabar: \n\nIsmi : ' + ism + '\nmanzili : ' + manzil + '\nTelefon Nomeri : ' + phone
    url = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id='
    requests.get(url + '737496239' '&text=' + text)

    return redirect('/')

def CreatePost(request):


    rasm = request.FILES['rasm']
    narx = request.POST['narx']

    Pictures.objects.create(rasm=rasm, narx=narx)

    return redirect('/')

