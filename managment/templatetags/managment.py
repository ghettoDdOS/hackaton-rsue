from django import template

from ..models import Case, Dates, Document, Sponsors

register = template.Library()


@register.simple_tag
def document_cards() -> dict:
    objects = Document.objects.all()

    return objects


@register.simple_tag
def dates_cards() -> dict:
    dates = Dates.objects.all()

    return dates


@register.simple_tag
def case_cards() -> dict:
    cases = Case.objects.all()

    return cases


@register.simple_tag
def sponsors_cards() -> dict:
    sponsors = Sponsors.objects.all()

    return sponsors
