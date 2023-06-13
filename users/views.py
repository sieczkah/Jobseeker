from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.decorators.debug import sensitive_variables


# Create your views here.
@sensitive_variables("username", "pw")
def login_view(request):
    # Page name to handle the login/register template
    page = "login"

    # Avoiding log in users login page via url
    if request.user.is_authenticated:
        return redirect("home")

    # Checking if request is POST, authenticating user and login in if authenticated
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            redirect_link = request.GET.get("next", default="home")
            return redirect(redirect_link)
    else:
        form = AuthenticationForm()

    context = {"page": page, "form": form}
    return render(request, "users/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("login")


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("home")
    else:
        form = UserCreationForm()

    context = {"form": form}
    return render(request, "users/login.html", context)
