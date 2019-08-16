from django import template

register = template.Library()

@register.filter
def add_value(field, value):
    return field.as_widget(attrs={"value": value})

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
