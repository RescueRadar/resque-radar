from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import requests
from django.http import JsonResponse
from agency.models import agency, non_approved_agency,Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import agency_req
from .forms import ContactForm, PostForm
from django.core.mail import send_mail
import os
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
import folium
from django.db.models import Q


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        if agency.objects.filter(user=request.user).exists():
            return redirect('dashboard')
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            EmailMessage(
                'New contact form submission',
                render_to_string('email/contact_form.html', {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'message': message
                }),
                os.environ.get('EMAIL_HOST_USER'),
                [os.environ.get('EMAIL_HOST_USER')],
                reply_to=[email]
            ).send()

            return redirect('home')
        else:
            print(form.errors)
    
    form = ContactForm()
    return render(request, 'contact.html',{
        'form': form
    })

def user_report(request):
    return render(request, 'user_report.html')

def error_message(request, error_message):
    return render(request, 'error_message.html', {'error_message': error_message})

def profileEdit(request):
    return render(request, 'profileEdit.html')

@login_required
@agency_req
def victims_portal(request):
    return render(request, 'victims_portal.html')

@login_required
@agency_req
def rooms(request):
    return render(request, 'rooms.html')

@login_required
@agency_req
def chatroom(request):
    return render(request, 'chatroom.html')

@login_required
def agencyPage(request):
    return render(request, 'agencyPage.html')

@login_required
@agency_req
def dashboard(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    posts = Post.objects.filter(
                Q(title__icontains=q) | 
                Q(content__icontains=q) 
            )
    return render(request, 'dashboard.html', {'posts': posts})

@login_required
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


@login_required
def all_agencies(request):
    all_agencies = agency.objects.all()
    return render(request, 'all_agencies.html', {'all_agencies': all_agencies})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

@login_required
@agency_req
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.agency = agency.objects.get(user=request.user)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})
    
@login_required
@agency_req
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.agency.user != request.user:
        return error_message(request, 'You are not allowed to edit other agency posts!')  
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

@login_required
@agency_req
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.agency.user != request.user:
        return error_message(request, 'You are not allowed to delete other agency posts!')
    post.delete()
    return redirect('dashboard')

@login_required
def display_map(request):
    # took sample data for rescue agencies location at puri (Odisha)
    data = [
        {"name": "NDRF", "latitude": 19.798306, "longitude": 85.826355},
        {"name": "DMDA", "latitude": 19.804039, "longitude":85.817136},
        {"name": "CDRI", "latitude": 19.794752, "longitude":85.812241},
        {"name": "ANC", "latitude": 19.809553, "longitude":85.795681},
        {"name": "RDA Volunteers", "latitude": 19.806808, "longitude":85.856833},
        {"name": "MKLO", "latitude": 19.803623, "longitude": 85.779922},
    ]

    m = folium.Map(location=[data[0]["latitude"], data[0]["longitude"]], zoom_start=5)

    for item in data:
        folium.Marker(
            location=[item["latitude"], item["longitude"]],
            popup=item["name"]
        ).add_to(m)

    bounds = [[item["latitude"], item["longitude"]] for item in data]
    m.fit_bounds(bounds)

    map_html = m._repr_html_()

    return render(request, 'display_map.html', {"map_html": map_html})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_ip_info(request):
    user_ip = get_client_ip(request)

    api_token = os.environ.get('IP_INFO_API')
    api_url = f'https://ipinfo.io/{user_ip}/json?token={api_token}'
    
    response = requests.get(api_url)
    if response.status_code == 200:
        ip_info = response.json()
        loc_info = ip_info.get('loc', '').split(',')
        latitude = loc_info[0] if len(loc_info) > 0 else ''
        longitude = loc_info[1] if len(loc_info) > 1 else ''
        city = ip_info.get('city', '')
        region = ip_info.get('region', '').strip('(), ') 
        postal = ip_info.get('postal')
        return {
            'latitude': latitude,
            'longitude': longitude,
            'city': city,
            'region': region,
            'postal': postal
        }

def display_ip_info(request):
    ip_info = get_ip_info(request)
    return render(request, 'sam.html', {'ip_info': ip_info})