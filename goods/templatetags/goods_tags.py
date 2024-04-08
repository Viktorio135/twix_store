from django import template

register = template.Library()


@register.simple_tag()
def discount_price(price, discount):
    return float(price) - (float(price) * float(discount)/100)
