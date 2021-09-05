from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from second_app.models import User
from second_app.forms import UserForm

# Create your views here.
def index(request):
    return HttpResponse('<h1>HELLO THERE, GENERAL GRIEVOUS</h1>')

def help(request):
    help_context = {"help":"this is the help variable test"}
    return render(request, 'second_app/help.html', context=help_context)

def user(request):
    # user_context = {'users':User.objects.all()}
    form = UserForm()
    print(request.POST)
    if request.method == 'POST':
        form = UserForm(request.POST)
        print('second printout: ', form)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    form_context = {'form': form}
    return render(request, 'second_app/users.html', context=form_context)