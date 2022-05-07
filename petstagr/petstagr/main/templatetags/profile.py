from django import template

from petstagr.main.models.profile_model import Profile

register = template.Library()


@register.simple_tag()
def has_profile():
    return Profile.objects.count() > 0
