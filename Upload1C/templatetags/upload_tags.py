from django import template
import Upload1C.views as views

register = template.Library()


@register.simple_tag()
def get_base():
    return views.base_db
