from django import template

register = template.Library()

@register.filter
def add_value(field, value):
    return field.as_widget(attrs={"value": value})