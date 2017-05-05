from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.contrib import messages, auth

import sys

from .models import Token

# Create your views here.
def send_login_email(request):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse('accounts:login') + '?token=' + str(token.uid)
    )
    message_body = 'Use this link to log in:\n\n%s' % (url,)
    print(type(send_mail))
    send_mail(
        'Your login link for Superlists',
        message_body,
        '263487967@qq.com',
        [email],
    )
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in."
    )
    return redirect('/')
    
    
def login(request):
    user = auth.authenticate(uid=request.GET.get('token'))
    if user:
        auth.login(request, user)
    return redirect('/')