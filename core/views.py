from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site
from user.tokens import account_activation_token
from django.core.mail import send_mail, EmailMultiAlternatives

from django.template.loader import get_template, render_to_string
from django.template import Context

from user.models import User
from product.models import Product

from user.forms import CustomUserCreationForm, CustomUserChangeForm


def home(request):
    product = Product.objects.all()
    return render(request, 'core/home.html', {'products': product})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('registration/signup_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            send_mail(mail_subject, message,
                      'salmansiddik19@gmail.com', [to_email])
            return redirect('signup_confirm')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form, })


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('signup_complete')
    else:
        return HttpResponse('Activation link is invalid!')


def signup_confirm(request):
    return render(request, 'registration/signup_confirm.html', {})


def signup_complete(request):
    return render(request, 'registration/signup_complete.html', {})
