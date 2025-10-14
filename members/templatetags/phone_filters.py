from django import template

register = template.Library()

@register.filter
def format_phone(value):
    digits = str(value)
    return f'{digits[:3]}-{digits[3:6]}-{digits[6:]}'
