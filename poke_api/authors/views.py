from django.shortcuts import render
from .forms import Register_user

def register_view(request):
    if request.POST:
        form = Register_user(request.POST)
    else:
        form = Register_user
    return render(request,'pages/register_view.html',{
        'form' : form
    })

# Create your views here.
