import functools
from django.shortcuts import redirect

def agency_req(view_func, redirect_url="accounts:profile"):
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.agency:
            return view_func(request,*args, **kwargs)
        return redirect(redirect_url)
    return wrapper