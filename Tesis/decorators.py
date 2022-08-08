from functools import wraps
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group


def custom_login_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        user = request.user
        LOGIN_URL = '/'
        user_groups = Group.objects.values_list("name", flat=True)
        if 'Estudiante' in user_groups:
            LOGIN_URL = '/'
        else:
            LOGIN_URL = 'docente/'

        return view_func(request, *args, **kwargs)
        return redirect(LOGIN_URL)
    return wrapped_view