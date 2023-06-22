from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


def allowed_users(allowed_groups=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            user_group = None
            if request.user.groups.exists():
                user_group = request.user.groups.all()[0].name

            if user_group in allowed_groups:
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied

        return wrapper_func

    return decorator
