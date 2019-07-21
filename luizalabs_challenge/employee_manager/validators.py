import re

from django.core.exceptions import ValidationError

def validate_phone_number(value):
    expression = r'^\([1-9]{2}\) (?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}$'
    if not bool(re.match(expression, value)):
        raise ValidationError("Phone number must have this format '(xx) xxxxx-xxxx'.")

def validate_name(value):
    if bool(re.search(r'\d', value)):
        raise ValidationError("Name should not contains digit.")
