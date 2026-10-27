from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import SignupForm, VolunteerApplicationForm
from .models import Profile


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user=user,
                full_name=form.cleaned_data["full_name"],
                phone=form.cleaned_data.get("phone", ""),
                area=form.cleaned_data.get("area", ""),
                blood_group=form.cleaned_data.get("blood_group", ""),
            )
            login(request, user)
            return redirect("core:home")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})


@login_required
def apply_role(request):
    if request.method == "POST":
        form = VolunteerApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return redirect("accounts:application_status")
    else:
        form = VolunteerApplicationForm()
    return render(request, "accounts/apply_role.html", {"form": form})

# Create your views here.
