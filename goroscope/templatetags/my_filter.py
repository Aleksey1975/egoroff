from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()


@register.filter(name='my_upper')
@stringfilter
def my_upper(value, count=1):
    return value.upper() * int(count)


@register.filter(name='my_split')
@stringfilter
def my_split(value, key=' '):
    return value.split(key)[0]
