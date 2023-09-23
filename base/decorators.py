import functools
from django.shortcuts import redirect
from agency.models import agency

def agency_req(view_func, redirect_url="home"):
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if agency.objects.filter(user=request.user).exists():
            return view_func(request,*args, **kwargs)
        return redirect(redirect_url)
    return wrapper