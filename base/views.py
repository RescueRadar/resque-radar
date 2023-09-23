from django.shortcuts import render
from agency.models import non_approved_agency

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')



def profile(request):
    if request.method=="POST":
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        website = request.POST['website']
        about = request.POST['about']
        location_lat = request.POST['location_lat']
        location_long = request.POST['location_long']
        locality = request.POST['locality']
        city = request.POST['city']
        state = request.POST['state']
        manpower = request.POST['manpower']
        volunteers = request.POST['volunteers']
        category_of_calamity = request.POST['category_of_calamity']
        category_of_service = request.POST['category_of_service']
        non_approved_agency.objects.create(name=name, address=address, phone=phone, email=email, website=website, about=about, location_lat=location_lat, location_long=location_long, locality=locality, city=city, state=state, manpower=manpower, volunteers=volunteers, category_of_calamity=category_of_calamity, category_of_service=category_of_service)
        return render(request, 'profile.html')
    return render(request, 'profile.html')
