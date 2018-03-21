from . models import Contacts,About,House,Category
# from .forms import NewHouseForm
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'index.html')


def search_results(request):
    if 'house' in request.GET and request.GET["house"]:
        search_term = request.GET.get("house")
        searched_houses = Image.search_by_category(search_term) 

        message = f"{search_term}"
        context = {
            "message":message,
            "houses":searched_houses

        }

        return render(request, 'search.html', context) 
    else:
        message = "You haven't searched for any term"
        context = {
            "message":message

        }
        return render(request, 'search.html',context) 
def home(request):
   
    house = House.objects.all()
    context = {
    "house" : house
    }

    return render(request, 'home.html', context)   
def about(request):
   
    about = About.objects.all()

    context = {
     "about" : about
    }

    return render(request, 'about.html', context)
def contact(request):
   
    contact = Contacts.objects.all()

    context = {
     "contact" : contact
    }

    return render(request, 'contact.html', context) 


def house_details(request, id):
    house = get_object_or_404(House, id=id)
    context ={
        "house" : house
    }

    return render(request, 'house_details.html', context)

# @login_required(login_url='/accounts/login/')
# def new_house(request):
#     form = NewHouseForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         new_house = form.save(commit=False)
#         new_house.save()
#         messages.success(request, "Successfully created")
#         return redirect('/')
#     else:
#         messages.error(request, "Not successfully created")

#     context = {
#         "form" : form,
#     }

#     return render(request, 'house_form.html', context)