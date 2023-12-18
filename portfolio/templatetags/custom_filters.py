from django.template import Library

register = Library()

@register.filter(name='truncate')
def truncate(value, arg):
    words = value.split()
    if len(words) > arg:
        return ' '.join(words[:arg])
    else:
        return value
    

@register.filter(name='split')   
def split(value, arg):
    temp1 = value.split(arg)[0]
    temp2 = value.split(arg)[1]
    return temp1, temp2
