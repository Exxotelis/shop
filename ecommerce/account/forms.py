from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'This email is invalid, Please try another one.')
        if len(email >= 350):
            raise forms.ValidationError(
                'Email must be greater than 350 characters.')
        return email


# Compare this snippet from ecommerce/account/views.py:
# from django.shortcuts import render
# from django.http import HttpResponse
# from .forms import UserRegisterForm
#
# # Create your views here.
#
#
# def register(request):
#     form = UserRegisterForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'account/register.html', context)
# Compare this snippet from ecommerce/account/templates/account/register.html:
# {% extends 'base.html' %}
# {% load static %}
# {% block title %}
# <title>Register</title>
# {% endblock %}
# {% block content %}
# <div class="container">

#     <div class="row">
#         <div class="col-md-6 mx-auto">
#             <div class="card card-body mt-5">
#                 <h2 class="text-center">Register</h2>
#                 <form action="" method="POST">
#                     {% csrf_token %}
#                     {{ form.as_p }}
#                     <button class="btn btn-primary btn-block">Register</button>
#                 </form>
#             </div>
#         </div>
#     </div>
# </div>
# {% endblock %}
