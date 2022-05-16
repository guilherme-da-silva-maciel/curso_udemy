from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import Register_user
from django.http import Http404

def register_view(request):
    register_form_data = request.session.get('register_form_data',None)
    form = Register_user(register_form_data)
    return render(request,'pages/register_view.html',{
        'form' : form
    })
    
def create_view(request):
    if not request.POST:
        raise Http404


    POST = request.POST

    request.session['register_form_data'] = POST

    form = Register_user(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()

        
        messages.success(request,'your user is created! , please log in.')

        del(request.session['register_form_data'])

    return redirect('authors:register')

# Create your views here.
