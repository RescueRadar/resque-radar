from django.shortcuts import render, redirect
from agency.models import agency, non_approved_agency
from django.contrib.auth.decorators import login_required
from .decorators import agency_req
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


@login_required
def profile(request):
    if request.method=="POST":
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.user.email
        website = request.POST['website']
        about = request.POST['about']
        # location_lat = request.POST['location_lat']
        # location_long = request.POST['location_long']
        # locality = request.POST['locality']
        city = request.POST['city']
        state = request.POST['state']
        manpower = request.POST['manpower']
        volunteers = request.POST['volunteers']
        # category_of_calamity = request.POST['category_of_calamity']
        # category_of_service = request.POST['category_of_service']
        non_approved_agency.objects.create(user=request.user, name=name, address=address, phone=phone, email=email, website=website, about=about, city=city, state=state, manpower=manpower, volunteers=volunteers)
        return redirect('profile')
    else:
        if non_approved_agency.objects.filter(user=request.user).exists():
            return render(request, 'request_submitted.html')
        elif agency.objects.filter(user=request.user).exists():
            return redirect('home')
        return render(request, 'profile.html')
