import json
from django.shortcuts import redirect
from user.models import User
from user.forms import LoginForm, RegisterForm
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView
from django.urls import reverse
from django.contrib.auth import logout as log_out



class UsersView(ListView):
    paginate_by = 2
    model = User
    template_name = "users.html"


class RegisterView(FormView):
    template_name = "register.html"
    form_class = RegisterForm
    # success_url = "/user/"

    def get_success_url(self) -> str:
        next_url = self.request.GET.get("next")
        if next_url is not None:
            return next_url
        return reverse("all_users")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def login(request):
    if request.user.is_authenticated:
        return redirect("all_users")
    context = {"login_form": LoginForm()}
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login_form.auth(request)
            return redirect("all_users")
        context.update(login_form=login_form)
    return render(request, "login.html", context)



def logout(request):
    log_out(request)
    return redirect("all_users")
