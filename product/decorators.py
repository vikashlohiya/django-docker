from django.shortcuts import redirect
from functools import wraps

def login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/login')  # Replace 'login' with the URL name of your login page
        return view_func(request, *args, **kwargs)
    return _wrapped_view
