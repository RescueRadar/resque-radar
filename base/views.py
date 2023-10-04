from django.shortcuts import render, redirect, get_object_or_404
from agency.models import agency, non_approved_agency,Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import agency_req
from .forms import ContactForm, PostForm
from django.core.mail import send_mail
import os
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

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
    all_agencies = agency.objects.all()
    return render(request, 'dashboard.html', {'all_agencies': all_agencies})

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
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

@login_required
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
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.agency.user != request.user:
        return redirect('post_list')  # Redirect if trying to edit other agency's post
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
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.agency.user != request.user:
        return redirect('post_list')  # Redirect if trying to delete other agency's post
    post.delete()
    return redirect('post_list')