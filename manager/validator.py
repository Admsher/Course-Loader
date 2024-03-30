# validators.py

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

def validate_password_similarity(username, password):
    if password and username.lower() in password.lower():
        raise ValidationError(
            _("The password is too similar to the username."),
            code='password_too_similar'
        )
