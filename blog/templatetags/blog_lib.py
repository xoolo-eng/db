from django import template


register = template.Library()

@register.filter(name="range")
def range_f(value, arg=1):
    return range(int(arg), int(value) + 1)