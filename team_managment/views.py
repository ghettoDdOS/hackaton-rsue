from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from managment.models import CoreSettings

from .forms import ParticipantsForm, TeamsForm


def index(request):
    settings = CoreSettings.objects.all()
    return render(request, "base.html", {"settings": settings})


def register(request):
    if request.method == "POST":
        form = ParticipantsForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.save()
            return HttpResponse(
                "<h1 style='font-family: Golos, Roboto, Arial;text-align: center;margin-top: 150px; color: #31498B; '>Ваша заявка успешно сохранена!</h1>\r\n<div style='font-family: Golos, Roboto, Arial;text-align: center;color: blue'><a href='/'>Вернуться на главную страницу</a></div>"
            )
    else:
        return render(
            request,
            "registration.html",
            {
                "form": ParticipantsForm,
                "title": "Вступить в существующую команду",
            },
        )


def register_team(request):
    if request.method == "POST":
        form = TeamsForm(request.POST)

        if form.is_valid():
            instance = form.save()
            instance.save()
            return HttpResponseRedirect("/registration")
    else:
        return render(
            request,
            "registration.html",
            {
                "form": TeamsForm,
                "title": "Регистрация команды",
            },
        )
