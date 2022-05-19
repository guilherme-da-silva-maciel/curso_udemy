from django.core.exceptions import ValidationError
import re

def add_attr(field,attr_name,attr_new_value):
    existing_attr = field.widget.attrs.get(attr_name,'')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_value}'.strip()

def add_placeholder(field,placeholder_val):
    add_attr(field,'placeholder',placeholder_val)


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError(
            'The password must be at least eight characters long, including at least one number or special character, and must not be too common.',
            code='Invalid'
        )
