from django import forms

from .models import Participants, Teams


class ParticipantsForm(forms.ModelForm):
    class Meta:
        model = Participants
        fields = [
            "first_name",
            "last_name",
            "patronymic",
            "email",
            "phone",
            "team",
        ]
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control w-50"},
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control w-50"},
            ),
            "patronymic": forms.TextInput(
                attrs={"class": "form-control w-50"},
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control w-50"},
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "form-control w-50",
                    "placeholder": "+7 (___) ___-__-__",
                    "pattern": "+7([0-9]{3})[0-9]{3}-[0-9]{2}-[0-9]{2}",
                    "id": "phone1",
                    "type": "tel",
                },
            ),
            "team": forms.Select(
                attrs={"class": "form-control w-50"},
            ),
        }


class TeamsForm(forms.ModelForm):
    class Meta:
        model = Teams
        fields = [
            "team_name",
            "organization",
            "direction",
        ]
        widgets = {
            "team_name": forms.TextInput(
                attrs={"class": "form-control w-50"},
            ),
            "organization": forms.TextInput(
                attrs={"class": "form-control w-50"},
            ),
            "direction": forms.Select(
                attrs={"class": "form-control w-50"},
            ),
        }
