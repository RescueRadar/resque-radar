from django.shortcuts import render, redirect
from agency.models import agency, non_approved_agency
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import agency_req
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def user_profile(request):
    return render(request, 'user_profile.html')

def profile(request):
    form_submitted = False
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.user.email
        website = request.POST.get('website')
        about = request.POST.get('about')
        city = request.POST.get('city')
        state = request.POST.get('state')
        manpower = request.POST.get('manpower')
        volunteers = request.POST.get('volunteers')

        form_submitted=True 

        if not all([name, address, phone, website, about, city, state, manpower, volunteers]):
            messages.error(request, "All fields must be filled.")
            return redirect('profile')

        
        non_approved_agency.objects.create(
            user=request.user,
            name=name,
            address=address,
            phone=phone,
            email=email,
            website=website,
            about=about,
            city=city,
            state=state,
            manpower=manpower,
            volunteers=volunteers
        )
        messages.success(request, "Profile information saved successfully.")
        form_submitted=True
        return redirect('request_submitted', form_submitted=str(form_submitted))  # Convert to string
    else:
        if non_approved_agency.objects.filter(user=request.user).exists():
            return redirect('request_submitted', form_submitted=form_submitted)
        elif agency.objects.filter(user=request.user).exists():
            return redirect('home')
        return render(request, 'profile.html', {'form_submitted': form_submitted})

def request_submitted(request, form_submitted):
    return render(request, 'request_submitted.html', {'form_submitted': form_submitted})