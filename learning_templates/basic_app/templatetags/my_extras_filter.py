from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value,args):
    """
    this cuts out all value of "args" in the string
    
    """
    return value.replace(args,'')

