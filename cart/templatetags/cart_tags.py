from django import template
from gde.models import Videogame, Dlc, Package

register = template.Library()

@register.filter()
def multiply(value, arg):
    return float(value) * arg

@register.filter()
def money_format(value, arg):
    return f"{value}{arg}"
