from django import template

register = template.Library()

#custom template filter
#using decorators
@register.filter(name='cut')
def cut(value,arg):
    """"
    cuts out values of arg from string
    """
    return value.replace(arg,'')
#normal methd
#register.filter('cut',cut)
