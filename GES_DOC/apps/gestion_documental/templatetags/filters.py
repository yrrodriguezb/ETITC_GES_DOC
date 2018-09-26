from django import template

register = template.Library()

@register.filter(name='get_text_from_index')
def get_text_from_index(value, character=None):
    if character is None:
        character = '/'

    index = value.rindex(character) + 1
    return value[index:]