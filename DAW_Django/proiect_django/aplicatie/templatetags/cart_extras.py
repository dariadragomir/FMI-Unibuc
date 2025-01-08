from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    return value * arg

@register.filter
def total_price(cart_items):
    return sum(item.instrument.pret * item.quantity for item in cart_items)

@register.filter
def total_quantity(cart_items):
    return sum(item.quantity for item in cart_items)