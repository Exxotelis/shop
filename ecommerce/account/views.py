from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CreateUserForm

# Create your views here.


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('')

    context = {
        'form': form
    }

    return render(request, 'account/registration/register.html', context)

# def register(request):
#     return render(request, 'account/registration/register.html')
